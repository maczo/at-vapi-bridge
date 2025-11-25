from flask import Flask, request, Response, url_for
import xml.etree.ElementTree as ET
import os

app = Flask(__name__)

@app.route('/voice-webhook', methods=['POST'])
def voice_webhook():
    caller = request.form.get('callerNumber', 'unknown')
    session_id = request.form.get('sessionId', 'unknown')
    print(f"Call from {caller} | Session: {session_id}")

    root = ET.Element('Response')

    # Optional super-fast greeting (remove these 4 lines if you want instant AI pickup)
    say = ET.SubElement(root, 'Say', {'voice': 'man', 'language': 'en-gb'})
    say.text = "One moment please…"

    # This is the ONLY line you ever change → your Vapi SIP address
    sip_uri = os.getenv('VAPI_SIP_URI')  # e.g., sip:mybot123@sip.vapi.ai

    ET.SubElement(root, 'Dial', {
        'number': sip_uri,
        'callerId': os.getenv('AT_PHONE_NUMBER'),  # your AT number, e.g. +2547…
        'timeout': '30',
        'action': url_for('voice_end', _external=True),
        'method': 'POST'
    })

    xml = '<?xml version="1.0" encoding="UTF-8"?>' + ET.tostring(root, encoding='utf-8', method='xml').decode()
    return Response(xml, mimetype='text/xml')

@app.route('/voice-end', methods=['POST'])
def voice_end():
    print("Call ended:", request.form.to_dict())
    return Response('<?xml version="1.0" encoding="UTF-8"?><Response></Response>', mimetype='text/xml')

@app.route('/health', methods=['GET'])
def health():
    return {"status": "healthy", "service": "at-vapi-bridge"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
