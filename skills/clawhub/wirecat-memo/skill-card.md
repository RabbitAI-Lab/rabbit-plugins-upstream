## Description:

Cli Memo finds what the owner knows about a person or project across Telegram, MAX, mail, and notes, and records facts, memories, and key documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operators use Cli Memo to answer questions about people, projects, agreements, and related records by searching stored messages, mail, notes, meetings, and business data. They can also add owner-provided sources and record or stage supported facts, memories, and documents through memo commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad searches can expose personal messages, mail, notes, or business records beyond the immediate question.

Mitigation: Keep searches focused on the user's request, use only the named accounts or group, and cite only relevant records.

Risk: CRM or financial record changes and identity merges may occur without a clear authorization step.

Mitigation: Review the target, account, amount, and identity match with the owner, and obtain explicit authorization before making or merging changes.

## Reference(s):

- [Cli Memo on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-memo)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)
- [@wirecat/cli-memo package](https://www.npmjs.com/package/@wirecat/cli-memo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown answers with memo record references and CLI commands where needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers cite stored records by their memo references; available coverage depends on the owner's stored and indexed sources.]

## Skill Version(s):

1.0.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
