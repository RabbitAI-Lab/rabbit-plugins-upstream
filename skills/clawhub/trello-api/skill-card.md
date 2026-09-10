## Description:

Trello API integration with managed OAuth for managing boards, lists, cards, members, and labels through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Trello for project management workflows such as listing boards, reading cards, creating or updating tasks, managing lists, labels, checklists, and members, and searching Trello content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent OAuth or API access can affect the connected Trello account beyond a single request.

Mitigation: Prefer OAuth, review requested Trello scopes during authorization, use least-privilege connections, and revoke unused connections.

Risk: Write and delete actions can modify or remove Trello boards, lists, cards, labels, checklists, or member assignments.

Mitigation: Default to read and list calls first, then require explicit user confirmation for every write or delete with the target resource and intended effect.

Risk: Installation uses unpinned third-party packages.

Mitigation: Use a constrained environment or pinned CLI versions when stricter supply-chain controls are required.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Trello API Overview](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)
- [Trello Boards API](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/)
- [Trello Cards API](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue Trello API calls through the Maton CLI after authentication and required user approvals.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
