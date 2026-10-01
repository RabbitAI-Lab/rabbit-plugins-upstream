## Description:

Helps an agent access and organize OneNote notebooks, sections, and pages through Microsoft Graph using a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to find and organize OneNote content, create or edit notes with approval, and optionally set up user-approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A new connection or write action could grant access to, change, or remove OneNote content.

Mitigation: Confirm the account, target, and intended changes with the user; prefer read-only access and least privilege.

Risk: Functions, triggers, or destinations can run later and forward event data automatically.

Mitigation: Review and approve each source, destination, account, and downstream action before enabling automation.

Risk: Exposed API keys or copied response data could disclose private information.

Mitigation: Keep credentials in the supported credential store and avoid printing keys or logging full responses.

## Reference(s):

- [Microsoft OneNote skill on ClawHub](https://clawhub.ai/byungkyu/skills/one-note)
- [Maton](https://maton.ai)
- [Microsoft Graph OneNote API overview](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Access requires a user-authorized OneNote connection; writes and automation require user approval.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
