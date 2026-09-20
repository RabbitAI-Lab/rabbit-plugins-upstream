## Description:

Manage Trello boards, lists, and cards via the Trello REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aperdigaokbk](https://clawhub.ai/user/aperdigaokbk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Trello boards, lists, and cards and to create, move, comment on, or archive cards through Trello REST API commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trello API keys and tokens may grant broad account access and are shown in URL query strings.

Mitigation: Use narrowly scoped or temporary credentials when available, keep credentials out of logs and shell history, and avoid sharing command output that includes query strings.

Risk: Create, move, comment, and archive commands can modify remote Trello boards and cards.

Mitigation: Verify board, list, and card IDs before running write operations and review commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aperdigaokbk/skills/trello)
- [Trello REST API documentation](https://developer.atlassian.com/cloud/trello/rest/)
- [Trello API key page](https://trello.com/app-key)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires jq plus TRELLO_API_KEY and TRELLO_TOKEN environment variables; Trello API rate limits apply.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
