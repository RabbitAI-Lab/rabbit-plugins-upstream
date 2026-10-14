## Description:

Turn a public TikTok stitch target into one quote reply card per chosen hook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and social media operators use this skill to turn a public TikTok video's caption and comments, or pasted quotes, into a plan and still-image reply cards using replies they wrote. It does not create stitched video or post replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra connection uses a shared device token and broad media and wallet permissions.

Mitigation: Review the requested access before connecting and use a trusted account and device.

Risk: Installation registration collects runtime telemetry.

Mitigation: Review the installation and authentication documentation before installing.

Risk: Installed package code can update silently by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` to keep reviewed code fixed.

Risk: Video lookups, comment pages, and image generation can consume credits.

Mitigation: Check live prices and confirm each paid lookup and generation separately before submitting.

## Reference(s):

- [Stitch Prompt Card release](https://clawhub.ai/beatra-ai/skills/stitch-prompt-card)
- [Stitch prompt workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Images]

**Output Format:** [Markdown cover plan and generated quote-reply image stills]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usually 1 to 6 stills (default 4); paid lookups and image generation require separate confirmation.]

## Skill Version(s):

0.1.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
