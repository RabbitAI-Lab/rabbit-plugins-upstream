## Description:

Find what the owner knows about a person or a project across Telegram, MAX, mail and notes through memo, and record facts, memories and key documents. Use when asked about a person, a project, what was agreed, or to search messages, mail and notes together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

People using the memo command line tool can search their selected messaging accounts, imported mail, and notes to answer questions about people, projects, and agreements. They can also stage cited facts and memories for owner review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches can expose private messages, mail, and notes from connected accounts.

Mitigation: Name only the intended source accounts and prefer read-only retrieval.

Risk: Mailbox rules or deletion can hide or remove stored mail.

Mitigation: Review previews and obtain the owner's approval before applying mailbox changes; the owner adds mail accounts themselves.

Risk: MCP's ask permission allows a write without displaying an interactive confirmation prompt.

Mitigation: Configure MCP write permissions deliberately and treat ask as authorization to run, not as an owner confirmation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wirecat/skills/wirecat-memo)
- [@wirecat/cli-memo on npm](https://www.npmjs.com/package/@wirecat/cli-memo)

## Skill Output:

**Output Type(s):** [Text, Shell commands]

**Output Format:** [Natural-language responses with cited references; memo can also return JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search coverage is account-scoped and may be bounded or incomplete; proposed records remain for owner review.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
