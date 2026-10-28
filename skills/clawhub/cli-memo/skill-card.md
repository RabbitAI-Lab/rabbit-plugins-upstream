## Description:

Find what the owner knows about a person or a project across Telegram, MAX, mail and notes through memo, and record facts, memories and key documents. Use when asked about a person, a project, what was agreed, or to search messages, mail and notes together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Owners and their agents use memo to search authorized messaging accounts, notes, and imported mail for information about people and projects, then record sourced facts, memories, and key documents for the owner to review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Imported private mailbox and messaging content persists in the local store.

Mitigation: Connect only accounts and folders intended for search; use read-only mode when only searching.

Risk: Mailbox cleanup can remove stored mail, and scheduled sync or remote access may expose or change the intended scope of access.

Mitigation: Review cleanup previews before applying them, and enable scheduled sync or remote access only when wanted.

Risk: Mail account setup involves sensitive credentials.

Mitigation: The owner adds mail accounts directly; the agent must never request mail or app passwords in chat.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wirecat/skills/cli-memo)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Cited text summaries and structured CLI JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include references and coverage metadata; proposals remain for owner review.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
