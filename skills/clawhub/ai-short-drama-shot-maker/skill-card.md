## Description:

Creates a cinematic vertical micro-drama shot from a defined dramatic beat, camera direction, and optional actor or scene references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan and generate one vertical live-action drama shot from text or approved images, then review the resulting video and shot continuity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared device authorization grants broad access to a Beatra account.

Mitigation: Review the requested account access and authorize only if comfortable sharing it with this package.

Risk: Silent automatic updates can replace local package files without a separate approval.

Mitigation: Review updates before use or disable automatic updates with `python3 scripts/mcp_client.py update --auto off`.

Risk: Video generation can spend Beatra credits.

Mitigation: Check the estimated cost and account balance, and obtain explicit approval before submitting a paid shot.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/ai-short-drama-shot-maker)
- [Beatra skill homepage](https://beatra.ai/skills/ai-short-drama-shot-maker)
- [Short-drama shot workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Video artifact references]

**Output Format:** [Markdown shot card and review with links or references to generated video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task status, available usage, and charges after generation.]

## Skill Version(s):

0.2.0 (source: ClawHub release and bundled manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
