## Description:

Systematically analyze, score, and optimize OpenClaw skill documents, adapting Microsoft SkillOpt research into validation-gated skill improvement workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[akdira](https://clawhub.ai/user/akdira)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to audit, score, and improve OpenClaw skill documents, including batch analysis and validation-gated optimization before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optimization and cron workflows can modify skill files across a workspace and may commit those changes.

Mitigation: Start with analyze-only use, review generated diffs manually, and avoid enabling cron or git auto-commit behavior unless a confirmation or dry-run gate is added.

Risk: Suggested edits could introduce incorrect or misleading guidance into skill documents.

Mitigation: Use validation-gated edits, review proposed changes before deployment, and scan optimized skills before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/akdira/skills/skill-optimizer)
- [SkillOpt Paper](https://arxiv.org/abs/2605.23904)
- [Microsoft SkillOpt Reference Implementation](https://github.com/microsoft/skillopt)
- [SkillOpt Paper Summary](references/skillopt-paper.md)
- [Meta Skill Patterns](references/meta-skill-patterns.md)
- [Skill Quality Rubric](templates/skill-quality-rubric.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown reports, shell commands, diffs, and optional updated SKILL.md files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analyze-only mode is read-only; optimize and cron modes may modify skill files and create reports.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
