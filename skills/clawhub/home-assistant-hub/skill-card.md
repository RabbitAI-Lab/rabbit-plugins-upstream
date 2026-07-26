## Description: <br>
Real-time Home Assistant monitoring, alert rules, TTS voice notifications on Echo devices, Telegram delivery, entity inspection. Service calls are HARD-DENIED by default and require explicit safe-domains opt-in. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincsta](https://clawhub.ai/user/vincsta) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Home Assistant operators use this skill to inspect home entities, configure alert rules, run a monitoring hub, deliver Telegram or Echo notifications, and invoke explicitly allowed Home Assistant services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a long-lived Home Assistant bearer token and Telegram credentials from config/hub.json. <br>
Mitigation: Protect config/hub.json with local file permissions, never commit it, and rotate Home Assistant or Telegram tokens if exposure is suspected. <br>
Risk: The default Home Assistant URL uses unencrypted HTTP traffic, which can expose credentials or telemetry on the local network. <br>
Mitigation: Change ha_url to HTTPS and WSS before adding a real token whenever the Home Assistant deployment supports it. <br>
Risk: Telegram alerts can reveal household routines, occupancy, and sensor states to an external service. <br>
Mitigation: Keep alert templates free of sensitive personal data and use Telegram delivery only for information suitable for that chat. <br>
Risk: Allowed Home Assistant service calls can change physical device state. <br>
Mitigation: Keep call_safe_domains limited to the smallest required set and use dry-run previews before enabling or executing state-changing calls. <br>


## Reference(s): <br>
- [Setup Guide](references/setup.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/vincsta/skills/home-assistant-hub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide background Node.js processes, Home Assistant API calls, Telegram delivery, and local configuration edits.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
