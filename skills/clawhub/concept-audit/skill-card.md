## Description:

Audits code against a concept model only when the user explicitly invokes $concept-audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to perform a read-only audit of code, specifications, tests, and related documentation against a concept model. It produces evidence-backed findings for drift, boundaries, criteria, composition, dependencies, and suggested repair routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads across a repository, specifications, tests, and related documentation to produce its audit.

Mitigation: Use it only on repositories where repository-wide read access is appropriate, and review the generated audit before acting on findings.

## Reference(s):

- [Concept Audit ClawHub Page](https://clawhub.ai/agenticweb4/skills/concept-audit)
- [Project Homepage](https://github.com/ontology-of-everything/SemanticSkills/tree/main/skills/concept-audit)
- [Composition Checklist](references/composition-checklist.md)
- [Drift Checklist](references/drift-checklist.md)
- [Sources](references/sources.md)
- [Criteria Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Sync Composition Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/sync/)
- [Concept Design Overview](https://essenceofsoftware.com/posts/distillation/)
- [Dependency Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/dependency/)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID Paper](https://arxiv.org/abs/2508.14511)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown audit report with evidence, impact, severity, and repair routing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output; no file modifications are performed by the skill.]

## Skill Version(s):

0.5.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
