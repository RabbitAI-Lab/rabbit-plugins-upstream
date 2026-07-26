## Description: <br>
Control Nest smart home devices such as thermostats, cameras, and doorbells through Google's Smart Device Management API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amogower](https://clawhub.ai/user/amogower) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Home automation users and agents use this skill to inspect Nest device status, adjust thermostat settings, generate camera streams, and receive doorbell or person-detection alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run a persistent public webhook that receives Nest event data. <br>
Mitigation: Install only when persistent monitoring is intended, authenticate and restrict the webhook, and review logs for sensitive event data. <br>
Risk: Doorbell and person alerts may send sensitive home camera images to Telegram or other third-party services. <br>
Mitigation: Enable photo alerts only where that sharing is acceptable, protect Telegram tokens, and use a controlled recipient chat. <br>
Risk: Nest credentials and refresh tokens can control physical devices and access camera streams. <br>
Mitigation: Use dedicated least-privilege credentials, store tokens securely, and rotate them if exposure is suspected. <br>
Risk: The webhook setup uses a Cloudflare tunnel binary and public endpoint. <br>
Mitigation: Verify the cloudflared binary, keep tunnel configuration minimal, and expose only the required webhook route. <br>


## Reference(s): <br>
- [ClawHub Nest Devices Skill](https://clawhub.ai/amogower/skills/nest-devices) <br>
- [Google Cloud Console](https://console.cloud.google.com) <br>
- [Google Nest Device Access Console](https://console.nest.google.com/device-access) <br>
- [Cloudflared Release Download](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute Nest SDM API actions and operate a webhook for Pub/Sub event handling when configured.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
