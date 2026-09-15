## Description:

Provides Have I Been Pwned lookup guidance through the OOMOL oo connector for searching breached accounts, listing paste exposures, retrieving breach records, listing data classes, and checking subscription status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run read-oriented Have I Been Pwned account, breach, paste, data-class, and subscription queries through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts without verification.

Mitigation: Do not let an agent run those installer commands automatically; use a trusted package source or manually inspect and verify installer contents before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-haveibeenpwned)
- [Have I Been Pwned homepage](https://haveibeenpwned.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
