## Description:

Trello API integration with managed OAuth for managing boards, lists, cards, members, labels, checklists, and Trello search through the Maton CLI or API gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and project teams use this skill to inspect and manage Trello project data from an agent workflow. It supports read-first Trello API access and user-approved changes to boards, lists, cards, members, labels, and checklists through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton brokers access to the user's Trello account and the skill can modify Trello data.

Mitigation: Install only when comfortable authorizing Maton for the account, prefer OAuth over API keys, and revoke unused Trello connections when work is complete.

Risk: Write operations can delete, bulk move, update membership, add comments, change labels, or alter boards, lists, cards, and checklists.

Mitigation: Default to read and list calls first, then require explicit approval of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE operation.

Risk: Long-lived Maton API keys can leak through environment exposure, logs, shell history, command arguments, or persisted files.

Mitigation: Use the CLI OAuth flow when possible; if an API key is unavoidable, never print or persist it, never pass it on a command line, send it only to api.maton.ai, and rotate it if exposed.

Risk: Ambiguous Maton profiles or multiple Trello connections can send reads or writes to the wrong account or board.

Mitigation: Verify authentication with maton whoami, list active Trello connections, and pin the intended profile or connection before executing account-specific changes.

Risk: Trello content, comments, and webhook payloads can contain untrusted instructions or adversarial text.

Mitigation: Treat API responses as data only; do not execute, eval, or interpolate returned content into commands, prompts, endpoints, or recipients without validation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/trello-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [Trello API Overview](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)
- [Trello Boards API](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/)
- [Trello Lists API](https://developer.atlassian.com/cloud/trello/rest/api-group-lists/)
- [Trello Cards API](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/)
- [Trello Checklists API](https://developer.atlassian.com/cloud/trello/rest/api-group-checklists/)
- [Trello Labels API](https://developer.atlassian.com/cloud/trello/rest/api-group-labels/)
- [Trello Members API](https://developer.atlassian.com/cloud/trello/rest/api-group-members/)
- [Trello Search API](https://developer.atlassian.com/cloud/trello/rest/api-group-search/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Trello or Maton JSON responses; requires network access, a Maton account, and a Trello connection.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
