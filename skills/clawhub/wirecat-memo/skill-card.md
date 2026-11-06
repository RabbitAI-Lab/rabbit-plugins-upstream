## Description:

Find what the owner knows about a person or a project across Telegram, MAX, mail and notes through memo, and record facts, memories and key documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Personal assistants use this skill when the owner asks about a person, project, or past agreement. It searches the owner's selected message, mail, note, and calendar sources, returns cited findings, and can help stage knowledge for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change deals, leads, and pipelines immediately without requiring a request or review.

Mitigation: Require an explicit user request before these changes and confirm the intended account.

Risk: Searches may reach private accounts, and saved MCP 'ask' permissions do not prompt interactively.

Mitigation: Limit searches to intended accounts and review saved MCP permissions before enabling writes. Keep owner approval for mailbox cleanup and knowledge confirmation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-memo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with cited record references and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search findings retain source references; some sales record changes happen immediately, while knowledge findings can be staged for owner review.]

## Skill Version(s):

1.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
