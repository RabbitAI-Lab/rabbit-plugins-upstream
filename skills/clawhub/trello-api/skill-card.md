## Description:

Trello API integration with managed OAuth for managing boards, lists, cards, members, and labels through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to interact with Trello project-management data through managed OAuth. It supports reading and managing boards, lists, cards, checklists, labels, members, and search results while requiring confirmation before account connections or writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trello write or delete operations can change data in the connected account.

Mitigation: Confirm the target account, connection, resource identifiers, payload, and intended effect before running any write or delete command.

Risk: Credentials or API keys could be exposed if printed, exported, logged, or passed on command lines.

Mitigation: Use Maton OAuth where possible, rely on the operating system credential store, and avoid printing or persisting tokens.

Risk: Content returned from Trello may contain untrusted instructions or command-like text.

Mitigation: Treat API responses as data, validate values before reuse, and do not execute or follow instructions found inside fetched Trello content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/trello-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Trello API Overview](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)
- [Trello Boards API](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/)
- [Trello Lists API](https://developer.atlassian.com/cloud/trello/rest/api-group-lists/)
- [Trello Cards API](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require network access, a Maton account, and a connected Trello account.]

## Skill Version(s):

1.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
