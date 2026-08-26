## Description:

为中国企业做 AI 与自动化落地机会初诊，并生成 Markdown、HTML、PDF 三种管理层报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xixisys](https://clawhub.ai/user/xixisys)

### License/Terms of Use:

MIT-0

## Use Case:

Business leaders, consultants, and enterprise AI practitioners use this skill to analyze Chinese enterprise materials, identify up to three practical AI or automation pilots, and generate management-ready diagnosis reports with evidence boundaries and human review requirements.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill processes business documents that may contain customer, employee, pricing, contract, production, or other confidential data.

Mitigation: Confirm that the agent may access the provided materials, limit inputs to necessary documents, and review generated reports before external sharing.

Risk: Generated reports include fixed consultation links to luodi.xixisys.com.

Mitigation: Review the report footer and call-to-action before distribution so recipients understand the third-party consultation destination.

Risk: AI recommendations could be mistaken for final business, staffing, legal, compliance, or safety decisions.

Mitigation: Keep human review for high-risk decisions and use the skill's evidence boundaries, unknowns, and pilot stop conditions before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xixisys/skills/enterprise-ai-opportunity-advisor-zh)
- [Deployment guidance](references/deployment-guidance.md)
- [Intake questionnaire](references/intake-questionnaire.md)
- [Report template](references/report-template.md)
- [Scoring rubric](references/scoring-rubric.md)
- [Task taxonomy](references/task-taxonomy.md)
- [Diagnosis output schema](schemas/diagnosis-output.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured JSON plus Markdown, HTML, and PDF report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a diagnosis JSON and renders three report formats from the completed analysis.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
