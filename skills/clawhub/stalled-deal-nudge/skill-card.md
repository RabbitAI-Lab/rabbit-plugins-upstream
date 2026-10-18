## Description:

Flags stalled open deals each Monday and posts a Slack digest per owner with recent activity, reasons to follow up, and drafts for reps to review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales reps and revenue operations teams use this skill to identify open deals without recent activity and review suggested follow-ups in a weekly Slack digest. The agent does not send messages to prospects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Digests can expose deal amounts, activity quotes, and drafted messages to unintended Slack readers.

Mitigation: Use an approved internal locked channel and verify the channel, bot membership, and owner mapping before deployment.

Risk: A CRM-backed adaptation may extract all deal and engagement records needed for selection.

Mitigation: Review data access and approve the CRM extraction scope before connecting it to a production workspace.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/stalled-deal-nudge)
- [Project homepage listed in release metadata](https://github.com/getcargohq/gtm-skills)
- [Digest format reference](artifact/references/digest.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Slack-formatted weekly digests with follow-up drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One digest per owner with stalled deals; drafts are for human review, not automatic delivery to prospects.]

## Skill Version(s):

0.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
