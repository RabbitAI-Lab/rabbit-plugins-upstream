## Description: <br>
Gets JFTech device livestream playback URLs for HLS, RTSP, RTMP, FLV, MP4, and WebRTC playback across web, mobile, and third-party players. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integrators use this skill to obtain authenticated livestream URLs for authorized JFTech devices and choose suitable playback protocols for web pages, WeChat mini programs, mobile apps, VLC, FFmpeg, or browser players. <br>

### Deployment Geography for Use: <br>
China mainland, Asia, Europe, and North America. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles live camera access URLs and device credentials without enough scoping or secret-handling safeguards. <br>
Mitigation: Use it only for devices the operator is authorized to access; keep JF_APP_SECRET, JF_DEVICE_TOKEN, device passwords, and returned livestream URLs out of chat logs, shell history, CI logs, and screenshots. <br>
Risk: Returned livestream URLs can remain reusable for the configured expiration period. <br>
Mitigation: Prefer short URL expirations and avoid sharing or storing returned playback URLs beyond the active troubleshooting or integration session. <br>
Risk: Setting JF_ENDPOINT to an untrusted host can send credentials and device access data to that host. <br>
Mitigation: Use only trusted JFTech API endpoints for the intended region, and do not override JF_ENDPOINT with untrusted hosts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-livestream) <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and Python script output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May output sensitive livestream URLs and operational guidance for selected protocols, streams, channels, and URL expiration windows.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
