## Description:

Audits an existing codebase against its Jackson concept model, including spec drift with calibrated severity checklists, boundaries, criteria, composition, dependencies, and cross-spec validation; read-only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit an existing codebase against Jackson concept specifications, identify drift and boundary issues, and route findings to the appropriate design, PRD, or implementation skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read broadly across the target repository to compare concept specs, PRDs, dependency material, and implementation code.

Mitigation: Run it only in repositories where broad read access is acceptable and review the generated findings before sharing them.

Risk: Most detailed instructions and report scaffolding are in Chinese, which may reduce review clarity for non-Chinese-speaking teams.

Mitigation: Have a reviewer fluent in the report language validate findings, routing, and severity before acting on the audit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/jackson-concept-audit)
- [Concept criteria tutorial](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Concept design overview](https://essenceofsoftware.com/posts/distillation/)
- [Dependency and subset tutorial](https://essenceofsoftware.com/tutorials/concept-basics/dependency/)
- [WYSIWID paper](https://arxiv.org/abs/2508.14511)
- [Beyond Objects paper](https://arxiv.org/abs/2606.27258)
- [jlifyio/wyx](https://github.com/jlifyio/wyx)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown audit report with findings tables and ordered remediation routing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only audit output; does not modify files.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
