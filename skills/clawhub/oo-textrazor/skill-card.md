## Description:

TextRazor lets an agent use an OOMOL-connected TextRazor account for content analysis, text classification, named-entity extraction, account quota checks, and custom classifier or dictionary management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route TextRazor tasks through an OOMOL-connected account for content analysis, classification, entity extraction, quota review, and custom classifier or dictionary operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes pipe-to-shell installation commands for the oo CLI.

Mitigation: Use safer oo CLI installation methods when possible and review the installer source before execution.

Risk: TextRazor tasks route content through an OOMOL-connected account.

Mitigation: Use the skill only when sending the content through OOMOL and TextRazor is acceptable for the user and organization.

Risk: Custom classifier and dictionary management can upload, overwrite, or delete TextRazor resources.

Mitigation: Require explicit confirmation of the exact operation, target, and payload before any write or destructive action.

## Reference(s):

- [ClawHub TextRazor skill page](https://clawhub.ai/oomol/skills/oo-textrazor)
- [TextRazor homepage](https://www.textrazor.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; connector runs return JSON when invoked with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
