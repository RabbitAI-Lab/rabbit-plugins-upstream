## Description:

Skill Upgrader helps an agent analyze, diagnose, and revise an existing OpenClaw skill using audit dimensions, upgrade phases, quality gates, and validation guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to improve one existing OpenClaw skill by auditing its purpose, reasoning, output quality, edge cases, references, and validation steps before applying a scoped upgrade.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A skill upgrade can change more of the target skill than intended.

Mitigation: Review the diff before accepting changes and confirm the run modified only the intended single skill.

Risk: Generated trigger rules could activate on unrelated requests if they are too broad.

Mitigation: Narrow trigger wording during review and reject generic activation language.

Risk: Skill revisions could accidentally touch sensitive credential or configuration files.

Mitigation: Follow the artifact guardrails: do not edit token, secret, credential, or protected metadata files, and verify the result with a diff and secret scan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-upgrader)
- [Skill anatomy](references/skill-anatomy.md)
- [Enhancement layers](references/enhancement-layers.md)
- [Quality standards](references/quality-standards.md)
- [Skill evolution](references/skill-evolution.md)
- [Skill upgrade template](templates/skill-upgrade-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured audit notes, checklists, templates, and proposed file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diff-style recommendations and validation steps; artifact metadata declares no required external binaries.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
