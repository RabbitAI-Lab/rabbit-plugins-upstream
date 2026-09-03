## Description:

Audits an existing codebase against its Jackson concept model for spec drift, boundary violations, criteria issues, composition quality, dependency rules, and cross-spec consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit existing repositories against Jackson concept specifications and PRDs. It produces a read-only findings report with severity, evidence, and routing to design, PRD, or implementation follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit reads repository specifications, PRDs, dependency documents, and implementation files, which may expose sensitive project context to the agent session.

Mitigation: Run it only where repository review is approved, and scope the request to relevant code and specification paths when possible.

Risk: Audit findings can be incomplete or misleading when concept specifications are missing, stale, or too numerous for manual review.

Mitigation: Require the report to state skipped dimensions and unverified categories, then independently review material findings before routing fixes.

Risk: The default artifact interface and much of the skill body are Chinese, which may be unsuitable for reviewers expecting English output.

Mitigation: Ask for the preferred output language before running the audit when review language matters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agenticweb4/skills/jackson-concept-audit)
- [Concept Criteria Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Concept Design Overview](https://essenceofsoftware.com/posts/distillation/)
- [Concept Dependency Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/dependency/)
- [WYSIWID Paper](https://arxiv.org/abs/2508.14511)
- [Beyond Objects Paper](https://arxiv.org/abs/2606.27258)
- [wyx Reference Implementation](https://github.com/jlifyio/wyx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown audit report with tables and an ordered remediation sequence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output; findings include locations, evidence, severity, and routing.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
