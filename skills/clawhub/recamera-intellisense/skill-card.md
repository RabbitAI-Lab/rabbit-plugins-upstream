## Description:

Register and control reCamera Pro devices from an agent, including camera onboarding, AI and sound detection, rule-based triggers, event polling with snapshots, media capture, storage management, app control, notification settings, video settings, and GPIO control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ichizer0](https://clawhub.ai/user/ichizer0)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect reCamera Pro hardware to agent workflows: registering devices, configuring AI or sound-triggered recording, retrieving events and media, and managing device settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send and persist camera bearer tokens over unverified or plaintext local discovery paths.

Mitigation: Use only cameras you own on trusted networks, prefer explicit registration with HTTPS and verified TLS, avoid RECAMERA_TOKEN auto-discovery unless transport behavior is understood, and protect or remove ~/.recamera/devices.json when finished.

Risk: Device operations can format storage, delete files, reboot cameras, change app lifecycle, control GPIO, and alter notify or recording rules.

Mitigation: Ask for explicit user confirmation before storage, reboot, file deletion, app lifecycle, GPIO, notify, or rule changes; rely on confirm=true gates only after that approval.

Risk: Captured media and relay URLs may expose camera content or short-lived unauthenticated access to large recordings.

Mitigation: Fetch imagery only when needed, avoid sharing relay URLs publicly, and treat returned snapshots, videos, and device paths as sensitive.

## Reference(s):

- [reCamera Pro Getting Started](https://wiki.seeedstudio.com/recamera_pro_getting_started/)
- [recamera-pysdk skill](https://github.com/Seeed-Studio/recamera-pro-ext-api/tree/main/skill/recamera-pysdk)
- [ClawHub skill page](https://clawhub.ai/ichizer0/skills/recamera-intellisense)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands invoke a bundled stdlib-only Python CLI; successful command executions return JSON on stdout.]

## Skill Version(s):

2.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
