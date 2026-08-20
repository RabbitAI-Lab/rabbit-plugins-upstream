## Description:

Rune is a 67-skill mesh for AI coding assistants that routes workflows across planning, implementation, review, testing, deployment, documentation, and domain-specific extension skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nhadaututtheky](https://clawhub.ai/user/nhadaututtheky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use Rune to coordinate AI coding-agent work across feature implementation, debugging, review, documentation, release, and repository-maintenance workflows. It is intended as a broad control layer that selects and combines specialized skills for software delivery tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rune is a broad coding-agent control layer whose routing, persistence, and external-tool use can affect sensitive repositories.

Mitigation: Install only when that level of agent control is intended, and review persisted .rune files periodically because they can influence later sessions.

Risk: Some workflows can involve deployment, GitHub issue or pull-request comments, destructive git operations, external AI CLI dispatch, or writes outside .rune.

Mitigation: Require explicit confirmation before allowing those high-impact operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nhadaututtheky/skills/rune-kit)
- [Rune documentation](https://rune-kit.github.io/rune)
- [Rune guides](https://rune-kit.github.io/rune/guides)
- [Artifact README](artifact/README.md)
- [Skill index manifest](artifact/skills/skill-index.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, command suggestions, configuration snippets, and task-specific checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs vary by routed subskill and may include proposed repository changes, verification steps, deployment instructions, or documentation updates.]

## Skill Version(s):

2.32.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
