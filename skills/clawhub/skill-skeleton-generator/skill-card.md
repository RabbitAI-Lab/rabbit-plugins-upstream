## Description:

Generates starter SKILL.md and AGENTS.md files for a new AI skill using a Python command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scaffold a new AI skill with starter metadata and agent-facing documentation, then edit the generated placeholders before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generating into a populated directory can overwrite existing SKILL.md or AGENTS.md files.

Mitigation: Run in a new or empty output directory and review the generated files before using them.

Risk: The permission metadata says filesystem access is unnecessary although the generator writes files.

Mitigation: Allow writes only to a dedicated output directory and verify the permissions required before installation.

Risk: The accompanying agent instructions claim JSON verdicts and PASS/FAIL behavior that the generator does not provide.

Mitigation: Do not treat the advertised verdicts as validation; inspect and validate generated files independently.

## Reference(s):

- [Skill Skeleton Generator on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/skill-skeleton-generator)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Shell commands]

**Output Format:** [SKILL.md and AGENTS.md files, with CLI status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated starter content contains placeholders requiring human editing.]

## Skill Version(s):

1.0.0 (source: ClawHub release; bundled SKILL.md lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
