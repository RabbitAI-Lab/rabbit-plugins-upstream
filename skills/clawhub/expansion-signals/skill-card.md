## Description:

Identifies renewal and expansion opportunities from customer purchase history and dated public events, records the findings on accounts, and sends a weekly Slack digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and account teams use this skill to identify customers nearing renewal, record evidence-backed expansion or at-risk signals, and share a prioritized weekly digest with the customer team.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer and renewal details may be shared through connected AI, web-search, or Slack services.

Mitigation: Review those services' data policies and confirm the configured Slack channel is internal before enabling the workflow.

Risk: Incorrect account judgments or unintended writes could affect account-team decisions.

Mitigation: Review the deployment plan, replace placeholder settings, and pilot on sample records with the play disabled before enabling recurring runs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/expansion-signals)
- [Publisher-listed project homepage](https://github.com/getcargohq/gtm-skills)
- [Example expansion plays](artifact/references/expansion-plays.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Text]

**Output Format:** [TypeScript resources, account signal fields, and a Slack-formatted weekly digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each account finding includes a signal, reason, and timestamp; the digest is limited to one post per week.]

## Skill Version(s):

0.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
