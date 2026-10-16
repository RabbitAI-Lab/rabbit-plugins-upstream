## Description:

Turns a novel chapter, web-novel excerpt, or story script into an ordered set of narrated vertical video scenes with illustrated, character-consistent shots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Story creators and publishers use this skill to adapt chapters or scripts into narrated, illustrated short-video scenes for book trailers, recaps, and story channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra device token has broad media and billing scopes, and installation registration is coarse.

Mitigation: Review the account access and registration implications before installing or authorizing the device.

Risk: The package silently updates local code by default.

Mitigation: Review this behavior before installing; disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if unwanted.

Risk: Image, speech, and video generation can incur credit charges.

Mitigation: Check the displayed estimate and explicitly approve paid calls, especially each video call, before submitting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/novel-promo-video-maker)
- [Beatra skill homepage](https://beatra.ai/skills/novel-promo-video-maker)
- [Novel promo workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Media artifacts]

**Output Format:** [Ordered scene descriptions and links to generated images, narration, and video clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports returned task status, media properties, usage, and net credits charged per scene.]

## Skill Version(s):

0.2.0 (source: server-resolved release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
