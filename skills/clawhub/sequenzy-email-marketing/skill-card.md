## Description:

Guides agents through Sequenzy email marketing operations, including authentication, subscriber management, campaigns, sequences, templates, transactional email, delivery stats, webhooks, inbox workflows, and supported workflow checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polnikale](https://clawhub.ai/user/polnikale)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing teams use this skill to help an agent choose and run supported Sequenzy CLI or MCP workflows for email marketing operations. It is most useful when the agent needs to inspect account state, manage contacts and audiences, draft or schedule email assets, handle transactional sends, review delivery data, or identify unsupported workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may operate with production Sequenzy credentials and affect real subscribers, campaigns, webhooks, or API keys.

Mitigation: Use least-privilege API keys and review the skill before installing it in an environment with production access.

Risk: Sends, scheduling, deletes, cancellations, webhook changes, and API-key creation or revocation can have immediate account impact.

Mitigation: Require explicit user confirmation for those actions and verify the exact recipient, campaign, sequence, webhook, or API-key target before execution.

Risk: Permanent campaign cancellation may be suggested without a confirmation step in some situations.

Mitigation: Inspect the campaign status and ID first, and require confirmation unless the user is explicitly asking to stop an active mistake immediately.

Risk: Ambiguous campaign or sequence IDs can cause the agent to act on the wrong resource.

Mitigation: Resolve and display the target resource before mutating it, and ask for clarification when identifiers or names are not unique.

## Reference(s):

- [Skill Source](artifact/SKILL.md)
- [Command Reference](artifact/references/command-reference.md)
- [Use Cases](artifact/references/use-cases.md)
- [ClawHub Skill Page](https://clawhub.ai/polnikale/skills/sequenzy-email-marketing)
- [ClawHub Publisher Profile](https://clawhub.ai/user/polnikale)
- [Sequenzy App](https://sequenzy.com)
- [Sequenzy API](https://api.sequenzy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and configuration examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce operational recommendations for live Sequenzy resources; review sensitive or destructive actions before execution.]

## Skill Version(s):

1.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
