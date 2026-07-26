## Description: <br>
Register and control reCamera Pro devices from an agent, including camera onboarding, AI and sound-event detection, rule-based triggers, event polling, image and video capture, recorded clip browsing, storage management, and GPIO control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ichizer0](https://clawhub.ai/user/ichizer0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to owned reCamera Pro hardware for device setup, model selection, detection rules, event monitoring, capture workflows, storage tasks, and GPIO operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control camera hardware, read and write camera files, format storage, change retention, and drive GPIO pins. <br>
Mitigation: Use it only with hardware you own and require explicit user approval before destructive storage changes, file deletion, retention changes, or GPIO writes. <br>
Risk: Long-lived bearer tokens and device profiles can grant access to registered cameras. <br>
Mitigation: Protect ~/.recamera/devices.json, avoid logging token values, and keep the profile file permission-restricted. <br>
Risk: Disabling TLS verification with allow_unsecured weakens transport security. <br>
Mitigation: Use allow_unsecured only for trusted LAN or self-signed local devices, and prefer HTTPS with trusted certificates on untrusted networks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ichizer0/skills/recamera-intellisense) <br>
- [Seeed Studio reCamera Pro getting started](https://wiki.seeedstudio.com/recamera_pro_getting_started/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON command examples, shell commands, and Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use a single JSON object argument and may return JSON, inline base64 media, URLs for larger files, or no stdout for some mutating operations.] <br>

## Skill Version(s): <br>
2.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
