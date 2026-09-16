## Description:

Audits concept and application design arguments and optional code conformance on explicit $concept-audit invocation, covering purpose fitness, independence, composition, drift, and product-subset review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review concept specifications, application synchronizations, and optional implementations for purpose fitness, independence, composition, drift, and product-subset coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to read project design documents and code during an audit.

Mitigation: Use it only in repositories where read-only design and conformance review is appropriate; do not provide credentials or ask it to install dependencies, make changes, or run background processes.

Risk: Audit conclusions can be incomplete when requirements, specifications, code, or tests are missing.

Mitigation: Mark unsupported conclusions as unverified and require current specification or code evidence for medium-or-higher severity findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/concept-audit)
- [ClawHub metadata homepage](https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/concept-audit)
- [Composition Defect Checklist](references/composition-checklist.md)
- [Specification Drift and Severity](references/drift-checklist.md)
- [Audit Sources](references/sources.md)
- [Concept and Synchronization Specification Contract](references/spec-format.md)
- [Concept Purposes and Synchronization](https://essenceofsoftware.com/posts/distillation/)
- [Concept Design Essay](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf)
- [Concept Qualification Criteria](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Concept Composition](https://essenceofsoftware.com/tutorials/concept-basics/sync/)
- [Concept Dependency](https://essenceofsoftware.com/tutorials/concept-basics/dependency/)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID](https://arxiv.org/abs/2508.14511)
- [wyx](https://github.com/jlifyio/wyx)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown audit report with an evidence table and fix routing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings should distinguish verified evidence from unsupported or unverified conclusions.]

## Skill Version(s):

0.5.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
