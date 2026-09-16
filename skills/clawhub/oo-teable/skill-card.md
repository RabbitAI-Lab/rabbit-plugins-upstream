## Description:

This skill operates Teable through an OOMOL-connected account for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Teable through an OOMOL-connected account, including listing spaces, bases, tables, and records, and creating, updating, or deleting table records when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager installation of the oo CLI and review installer contents before execution.

Risk: Create, update, and delete actions can change or permanently remove Teable records.

Mitigation: Confirm the exact payload, target table, target record, and expected effect with the user before running write or destructive actions.

Risk: The skill operates through the user's connected Teable scope.

Mitigation: Install only when the OOMOL publisher and the connected Teable account scope are trusted for the intended workspace.

## Reference(s):

- [Teable homepage](https://teable.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-teable)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
