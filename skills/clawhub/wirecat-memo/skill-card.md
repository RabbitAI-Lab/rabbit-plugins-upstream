## Description:

Find what the owner knows about a person or a project across Telegram, MAX, mail and notes through memo, and record facts, memories and key documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use Cli Memo to answer questions about a person or project by searching the owner's connected messages, mail and notes, and to record proposed facts, memories and key documents for the owner to review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches can expose private content from connected accounts and folders.

Mitigation: Connect only the accounts and folders the owner wants searched, and prefer read-only permissions unless changes are needed.

Risk: Mailbox cleanup can move matching mail to Trash.

Mitigation: Preview the affected mail and run deletion only after the owner approves.

## Reference(s):

- [Cli Memo on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-memo)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands and cited saved-item references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search responses report coverage; proposed record changes await owner review.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
