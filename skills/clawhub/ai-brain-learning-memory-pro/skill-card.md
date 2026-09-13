## Description:

Provides AI memory engineering methodology and a local evaluation script for designing, securing, and assessing agent memory systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent architects, and AI memory practitioners use this skill to turn memory-system methodology into implementation guidance, review schedules, poisoning defenses, and local JSON evaluation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install instructions may fetch mutable remote content after review.

Mitigation: Review or pin the exact repository commit or package version, and prefer installing this reviewed artifact into a project-scoped skill directory.

Risk: The local evaluation script reads a user-selected memory root and writes a results file.

Mitigation: Point the script only at memory folders intended for review, and inspect the generated JSON before using it to guide memory changes.

## Reference(s):

- [Research sources and engineering evidence](references/调研出处与证据.md)
- [Security audit](SECURITY_AUDIT.md)
- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-brain-learning-memory-pro)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with Python code examples and optional JSON evaluation output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The evaluation script is local-only and should be run manually against an intended memory root.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
