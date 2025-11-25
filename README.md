# Africa’s Talking → Vapi AI Bridge

When someone calls your AT number → instantly talks to your Vapi AI.

## One-line setup on Hetzner
1. Fork this repo
2. Go to https://hetzner.com/cloud → create a server (CX11 = €3/month is enough)
3. Choose "Docker" as the image → paste this repo URL → deploy
4. Copy your `.env.example` to `.env` and put your real values
5. Done!

Your webhook URL will be: https://your-server-ip-or-domain.com/voice-webhook

Paste that URL into Africa’s Talking dashboard → Voice → Callback URL.

Call your AT number → AI answers!
