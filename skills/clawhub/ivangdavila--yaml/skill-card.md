## Description:

Writes, debugs, and validates YAML that parses the same in every language and tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write, review, debug, validate, and safely edit YAML across configuration files, manifests, CI workflows, schemas, and tool-specific dialects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically stores and reuses local project and device metadata across sessions.

Mitigation: Install only if persistent local notes are acceptable; disable or clear records under ~/Clawic/data/yaml/, ~/Clawic/data/projects/, and ~/Clawic/data/devices/ when cross-session memory is not desired.

Risk: YAML files often contain secrets or private keys that could be copied into local notes.

Mitigation: Use the skill's pointer-only secret handling and confirm that credential values are stripped before any YAML details are saved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/yaml)
- [Clawic YAML skill page](https://clawic.com/skills/yaml)
- [YAML security guidance](artifact/security.md)
- [YAML parser guidance](artifact/parsers.md)
- [YAML schema and lint guidance](artifact/schemas.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code, YAML snippets, shell commands, diffs, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or revise local YAML files and local notes when the user requests durable configuration memory.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
