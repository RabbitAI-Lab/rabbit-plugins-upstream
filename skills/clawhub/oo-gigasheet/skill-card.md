## Description:

Gigasheet helps an agent search Gigasheet library metadata, inspect datasets, list exports and recent files, and check storage or enrichment-credit usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent perform authenticated, primarily read-only Gigasheet account operations such as dataset description, library search, export listing, and usage lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute arbitrary code.

Mitigation: Review the setup path before installing and prefer a trusted, versioned, verifiable oo CLI installation method.

Risk: The skill can inspect data in the connected Gigasheet account.

Mitigation: Use the skill only when account-data inspection is intended, and keep actions read-only unless the user explicitly approves a state-changing action.

## Reference(s):

- [ClawHub Gigasheet skill page](https://clawhub.ai/oomol/skills/oo-gigasheet)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Gigasheet homepage](https://www.gigasheet.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas to validate action payloads before execution.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
