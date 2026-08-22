## Description:

Register and control reCamera Pro devices from an agent for camera onboarding, AI and sound-event detection, rule-based triggers, event polling, capture, recordings, storage, and GPIO control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ichizer0](https://clawhub.ai/user/ichizer0)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent onboard, monitor, and control owned reCamera Pro devices. It supports device registration, model selection, event polling with snapshots, capture workflows, recording management, storage operations, and GPIO actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera recordings, snapshots, and returned relay URLs may expose sensitive footage.

Mitigation: Use the skill only with cameras and networks you control, avoid exposing relay URLs publicly, and treat returned media, URLs, and base64 payloads as sensitive data.

Risk: Clearing event history, formatting or removing storage, deleting files, rebooting devices, changing GPIO pins, or changing image settings can disrupt hardware or destroy data.

Mitigation: Require explicit user approval before these actions, target a named device, and pass confirmation flags only after the user has approved the specific operation.

Risk: Bearer tokens and unverified HTTPS connections can expose device credentials on an untrusted network.

Mitigation: Keep tokens out of logs and commits, use the protected device store, and set allow_unsecured only for trusted LAN devices with self-signed certificates.

## Reference(s):

- [reCamera Intellisense API Reference](REFERENCE.md)
- [Seeed Studio reCamera Pro Getting Started](https://wiki.seeedstudio.com/recamera_pro_getting_started/)
- [ClawHub Skill Page](https://clawhub.ai/ichizer0/skills/recamera-intellisense)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with bash invocations and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return inline base64 for small camera files and relay URLs or notes for larger recordings.]

## Skill Version(s):

2.1.1 (source: server release evidence and artifact __version__)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
