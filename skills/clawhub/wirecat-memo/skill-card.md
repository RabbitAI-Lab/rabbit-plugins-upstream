## Description:

Find what the owner knows about a person or a project across Telegram, MAX, mail and notes through memo, and record facts, memories and key documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to answer questions about a person's or project's history by searching the owner's selected messaging accounts, mail, and notes. They can also record proposed facts, memories, and key documents for the owner to review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches across personal messages, mail, and notes can expose information from accounts beyond the intended scope.

Mitigation: Limit searches to the accounts intended for the task and review returned coverage.

Risk: Mailbox changes and remote MCP writes can alter stored data, and remote writes may run under saved permissions without another prompt.

Mitigation: Review mailbox previews before approving changes, check saved permissions, and use MEMO_READ_ONLY=1 for retrieval-only work.

## Reference(s):

- [Cli Memo on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-memo)
- [@wirecat/cli-memo on npm](https://www.npmjs.com/package/@wirecat/cli-memo)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, JSON]

**Output Format:** [Text responses with source references; command results may be JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches are account-scoped and report coverage; recorded knowledge remains a proposal for owner review.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
