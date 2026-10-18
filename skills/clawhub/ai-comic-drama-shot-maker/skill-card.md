## Description:

Turns an approved comic panel, character sheet, or story beat into a short animated comic-drama shot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and their agents use this skill to plan and generate individual motion-comic shots from approved manga, webtoon, or character artwork, or from an approved original first frame.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra device token grants media-generation and spending authority.

Mitigation: Protect the local credential, review account spending controls, and approve each paid generation stage only after checking its live estimate.

Risk: Automatic package updates are enabled by default and may replace installed code without separate confirmation.

Mitigation: Review update behavior before installation and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if desired.

Risk: Installation registration sends limited installation and runtime information to Beatra.

Mitigation: Review the documented registration fields and privacy implications before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/ai-comic-drama-shot-maker)
- [Comic-drama shot workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Installation registration](references/installation-registration.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown with shot plans, task status, and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is delivered via returned artifacts or links; paid image and video stages require separate approval.]

## Skill Version(s):

0.2.1 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
