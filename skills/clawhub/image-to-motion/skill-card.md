## Description:

Animates a supplied still image into a short video clip with directed subject and camera motion while prioritizing recognizable details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to turn a supplied photo, product image, portrait, or artwork into a short motion clip for social content, product visuals, or storyboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared account authorization permits billable generation and may spend Beatra credits.

Mitigation: Review the live estimate and confirm adequate credits before submitting a paid request; authorize only an account where agent spending is acceptable.

Risk: Credentials persist across Beatra skills and the connection records registration or usage telemetry.

Mitigation: Review account access before connecting, keep the token private, and disconnect through the documented uninstall or account controls when no longer needed.

Risk: Automatic package updates are enabled by default and may change the installed skill without separate approval.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if unreviewed updates are unacceptable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/image-to-motion)
- [Motion brief, request, and recovery](artifact/references/workflow.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Video links, Guidance]

**Output Format:** [Markdown with a motion brief, task status, and video artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports actual credits charged after completion; video appearance may drift from the source image.]

## Skill Version(s):

0.2.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
