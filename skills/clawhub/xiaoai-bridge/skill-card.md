## Description:

Bridges Xiaomi Xiaoai speaker voice commands to OpenClaw, with trigger filtering, duplicate suppression, and spoken text-to-speech replies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[warm-winter](https://clawhub.ai/user/warm-winter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to route trigger-filtered speech from a Xiaomi Xiaoai speaker to an assistant and play the response back through the speaker. It also provides setup guidance and JSON message events for downstream consumers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaomi credentials and session files can provide access to account data and connected devices.

Mitigation: Use a dedicated non-administrator account, protect configuration and session files, leave the insecure-directory override disabled, and revoke or replace exposed credentials.

Risk: Voice transcripts may contain sensitive speech, and consequential voice-triggered actions need safeguards.

Mitigation: Avoid persisting transcript output or debug transcripts, and require confirmation before high-impact actions.

## Reference(s):

- [MiGPT-Next API Reference](references/migpt-api.md)
- [MiGPT-Next project](https://github.com/idootop/migpt-next)
- [xiaoai-bridge on ClawHub](https://clawhub.ai/warm-winter/skills/xiaoai-bridge)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON Lines voice-message events plus Markdown setup and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Events include original and trigger-filtered speech text and a millisecond timestamp.]

## Skill Version(s):

1.2.4 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
