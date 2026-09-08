## Description:

Audits a codebase against concept-model specifications for specification drift, concept independence, sync composition defects, criteria fit, dependency integrity, and fix routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering reviewers use this skill to inspect an existing codebase and concept/specification documents for drift, boundary violations, composition defects, and dependency issues, then receive evidence-backed findings with routed fix ownership.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to inspect the current codebase and concept/specification documents, so audit output may include sensitive repository details.

Mitigation: Use it only in workspaces where that inspection is intended, and review generated audit reports before sharing them outside the project.

Risk: Mentioning the skill name may activate it when a full concept audit was not intended.

Mitigation: Invoke it only when an audit is desired, and remove or disable the skill in environments where accidental activation would be disruptive.

Risk: The artifact and default interface include Chinese-language instructions, which may reduce clarity for non-Chinese users.

Mitigation: Ask the agent to produce the audit report in the user's preferred language when invoking the skill.

## Reference(s):

- [Drift Checklist](references/drift-checklist.md)
- [Composition Checklist](references/composition-checklist.md)
- [Skill Source Principles](references/sources.md)
- [Concept Criteria Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Sync Composition Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/sync/)
- [Concept Design Overview](https://essenceofsoftware.com/posts/distillation/)
- [Dependency and Subsets Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/dependency/)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID](https://arxiv.org/abs/2508.14511)
- [jlifyio/wyx](https://github.com/jlifyio/wyx)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown audit report with findings tables, evidence, severity, routing, systemic patterns, and ordered remediation steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analysis; does not modify files.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
