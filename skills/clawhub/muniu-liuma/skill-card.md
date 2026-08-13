## Description:

SDD workflow toolbox that helps agents choose and use five step-specific skills for spec writing, architecture design, task planning, implementation guidance, and completion auditing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[timeaground](https://clawhub.ai/user/timeaground)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to select the right SDD step skill and guide an agent through requirements clarification, architecture design, task breakdown, implementation guidance, and delivery auditing. It is most useful when a project needs structured handoffs between planning, design, implementation, and review work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Architecture and audit modes may inspect project files supplied by the user or available in the active workspace.

Mitigation: Run the skill only against intended project materials and avoid providing unrelated confidential files.

Risk: Generated architecture, dependency, configuration, database, or deletion guidance could be incorrect or too broad for the project context.

Mitigation: Review generated guidance before allowing a separate coding agent to make changes.

Risk: Audit results may depend on whether implementation evidence and test results are available.

Mitigation: Provide concrete artifacts and test outputs, and treat missing or unexecuted tests as unverified rather than accepted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/timeaground/skills/muniu-liuma)
- [Main toolbox overview](artifact/SKILL.md)
- [spec-writer skill](artifact/skills/spec-writer/SKILL.md)
- [arch-designer skill](artifact/skills/arch-designer/SKILL.md)
- [task-planner skill](artifact/skills/task-planner/SKILL.md)
- [impl-guide skill](artifact/skills/impl-guide/SKILL.md)
- [audit-trace skill](artifact/skills/audit-trace/SKILL.md)
- [Test skeleton specification](artifact/TEST-SKELETON-SPEC.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown by default, with optional JSON or CSV for supported workflow outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow outputs may include context-check markers, structured specs, ADRs, task tables, test skeletons, audit reports, installation guidance, and distribution guidance.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
