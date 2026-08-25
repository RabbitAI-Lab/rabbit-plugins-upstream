## Description:

基于合同修改经验识别房地产、建设工程和合作类合同中的风险条款，并提供风险等级和修改建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, business, and operations users review Chinese real estate, construction, procurement, installation, and cooperation contracts for risky clauses before negotiation or revision. The skill produces directional review suggestions and does not replace professional legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contracts may contain sensitive business terms or personal data.

Mitigation: Invoke the skill explicitly for intended contract-review work and review generated reports before sharing them.

Risk: The review output may be incomplete, overly broad, or unsuitable for a specific legal decision.

Mitigation: Treat the report as directional guidance and have a qualified lawyer review material contracts or major commercial decisions.

Risk: Pattern-based checks can miss relevant clauses or flag clauses that are acceptable in context.

Mitigation: Validate flagged clauses against the full contract, negotiation position, and applicable legal requirements before revising.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seairteng/skills/kt-legal-expert)
- [Artifact README](artifact/README.md)
- [Artifact skill instructions](artifact/SKILL.md)
- [Artifact changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown contract review report with risk levels, clause context, and prioritized revision suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reviews user-provided docx, txt, or md contract text and returns local suggestions for human review.]

## Skill Version(s):

1.0.1 (source: release evidence and artifact/CHANGELOG.md, released 2026-08-19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
