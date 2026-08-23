## Description:

Monitors Frigate NVR MQTT events and sends real-time WhatsApp and email notifications with camera snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rupertcachandler](https://clawhub.ai/user/rupertcachandler)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and home automation operators use this skill to connect Frigate camera detections to WhatsApp and email alerts, including identity-aware messages and event images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera snapshots and detection details may expose sensitive activity when sent to WhatsApp or email.

Mitigation: Configure only trusted recipients and run the notifier where people captured by cameras have appropriate notice or consent.

Risk: The local config.json contains SMTP credentials and notification targets.

Mitigation: Protect the configuration file with restrictive permissions, keep it out of source control, and rotate credentials if exposed.

Risk: Frigate API access can expose event images if the endpoint is insecure or unauthenticated.

Mitigation: Prefer HTTPS and authenticated Frigate access where available, and run the notifier only on trusted networks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rupertcachandler/skills/frigate-notifier)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local runtime configuration for MQTT, Frigate API, WhatsApp target, email target, SMTP credentials, and notification rate limits.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
