## Description: <br>
Zoom RTMS Meeting Assistant - start on-demand to capture meeting audio, video, transcript, screenshare, and chat via Zoom Real-Time Media Streams, handle RTMS webhook events, and provide AI-powered dialog suggestions, sentiment analysis, live summaries, and WhatsApp notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tanchunsiong](https://clawhub.ai/user/tanchunsiong) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and meeting operators use this skill to run a headless Zoom RTMS capture service that records meeting media, transcripts, screenshares, and chat, then produces AI summaries, dialog suggestions, and sentiment analysis. It is intended for Zoom RTMS webhook-triggered meeting recording and analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill records sensitive meeting audio, video, transcripts, screenshares, and chat. <br>
Mitigation: Obtain participant consent, restrict access to the recordings folder, and define retention and deletion rules before use. <br>
Risk: Webhook and notification controls may expose sensitive meeting data if reachable by unauthorized users. <br>
Mitigation: Restrict the webhook and toggle endpoints and verify Zoom webhook signatures before using the service for real meetings. <br>
Risk: Network controls need review before deployment. <br>
Mitigation: Remove disabled TLS validation and review Zoom RTMS connection handling before production use. <br>


## Reference(s): <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [ngrok unofficial webhook skill](https://github.com/tanchunsiong/ngrok-unofficial-webhook-skill) <br>
- [Zoom unofficial community skill](https://github.com/tanchunsiong/zoom-unofficial-community-skill) <br>
- [ClawHub skill page](https://clawhub.ai/tanchunsiong/skills/zoom-meeting-assistance-with-rtms-unofficial-community-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, plus generated transcript, summary, dialog, sentiment, notification, and media artifact files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Zoom RTMS credentials, a webhook endpoint, Node.js, ffmpeg, and OpenClaw; meeting recordings and analysis files are written under recordings.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
