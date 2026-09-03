## Description:

YouClaw helps marketers analyze ad creatives, uncover brand advertising strategies, and refine campaign ideas through YouCloud's YouShu AI service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcloud](https://clawhub.ai/user/youcloud)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and growth strategists use this skill to request brand, competitor, ad creative, audience, and campaign strategy analysis. It supports both full analysis reports and iterative creative critique workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt content is sent to an external YouCloud/YouShu service for marketing analysis.

Mitigation: Use the skill only for content approved for that service, and avoid sending sensitive campaign, brand, customer, or confidential business information unless your organization permits it.

Risk: Follow-up questions may reuse a previous API session.

Mitigation: Start a new request when switching brands, campaigns, clients, or sensitivity levels, and use explicit slash commands for sensitive workflows.

Risk: The skill requires a YOUCLOUD_API_KEY with access to the YouCloud/YouShu service.

Mitigation: Store the key in the environment, restrict access to authorized users, and rotate or revoke the key according to your credential-management policy.

## Reference(s):

- [Usage example](references/example.md)
- [YouCloud homepage](https://www.youcloud.com)
- [ClawHub skill page](https://clawhub.ai/youcloud/skills/youclaw)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Markdown analysis reports and configuration guidance, with shell commands for setup when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reuse a prior API session for follow-up questions; API requests require YOUCLOUD_API_KEY.]

## Skill Version(s):

1.2.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
