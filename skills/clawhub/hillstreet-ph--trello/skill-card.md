## Description:

Manage Trello boards, lists, and cards via the Trello REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to inspect Trello boards, lists, and cards, and to create, move, comment on, or archive cards through the Trello REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Trello API key and token provide full access to the user's Trello account.

Mitigation: Use the skill only when the release source is trusted, keep both credentials private, and review the target board, list, or card before running commands that change data.

## Reference(s):

- [Trello REST API documentation](https://developer.atlassian.com/cloud/trello/rest/)
- [Trello API key and token setup](https://trello.com/app-key)
- [Trello skill release on ClawHub](https://clawhub.ai/hillstreet-ph/skills/trello)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Guidance]

**Output Format:** [Markdown with curl command examples and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use user-provided Trello board, list, and card IDs and API credentials.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
