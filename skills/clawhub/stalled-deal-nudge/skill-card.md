## Description:

Produces weekly Slack digests of open deals without recent activity, including the last interaction, a reason to follow up, and a draft for the deal owner to send.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales representatives, sales leaders, and revenue operations teams use this skill to identify open deals with no logged activity for at least 14 days and prepare owner-specific follow-ups in a weekly Slack digest. Drafts are for representatives to review and send, not sent to prospects by the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deal amounts and customer or prospect quotes could be exposed in an unsuitable Slack channel.

Mitigation: Confirm the destination channel is internal and appropriate for sales data, and set its channel ID and owner mapping deliberately before deployment.

Risk: Untrusted activity notes or emails could steer the generated digest or ledger actions.

Mitigation: Treat activity text as untrusted data and test that embedded instructions do not change Slack output or ledger writes.

Risk: A CRM-backed adaptation may extract more customer data than the digest needs.

Mitigation: Review the fields and scope of any CRM-backed model before enabling it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/stalled-deal-nudge)
- [Project homepage (release metadata)](https://github.com/getcargohq/gtm-skills)
- [Digest format reference](artifact/references/digest.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Code]

**Output Format:** [Slack-formatted digest text with follow-up drafts; Markdown setup guidance and TypeScript configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One digest per owner with stalled deals per weekly run; draft messages require human review and sending.]

## Skill Version(s):

0.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
