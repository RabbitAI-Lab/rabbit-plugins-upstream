## Description:

Register and control reCamera Pro devices from an agent: onboard cameras, choose AI detection models, configure recording triggers, poll detection events with snapshots, capture media, browse recordings, manage storage, and drive GPIO pins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ichizer0](https://clawhub.ai/user/ichizer0)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect agent workflows to owned or administered reCamera Pro devices for detection, capture, recording, storage, and GPIO tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved device tokens and relay URLs can grant access to camera data.

Mitigation: Treat tokens and relay URLs as sensitive, do not log or share them, and install the skill only for cameras the user owns or administers.

Risk: Media capture, GPIO changes, storage operations, and device reboot can affect physical devices or stored recordings.

Mitigation: Review commands before execution and require explicit user intent before passing confirm=true for destructive operations.

Risk: Using unverified HTTPS is appropriate only for trusted local devices with self-signed certificates.

Mitigation: Keep TLS verification enabled by default and allow unsecured connections only on trusted LANs.

## Reference(s):

- [reCamera Intellisense API Reference](REFERENCE.md)
- [reCamera Pro Getting Started](https://wiki.seeedstudio.com/recamera_pro_getting_started/)
- [ClawHub skill page](https://clawhub.ai/ichizer0/skills/recamera-intellisense)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with command examples and JSON-oriented tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can write captures or downloaded files and device calls return JSON.]

## Skill Version(s):

2.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
