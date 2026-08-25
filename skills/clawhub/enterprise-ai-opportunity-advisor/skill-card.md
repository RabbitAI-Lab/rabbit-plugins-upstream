## Description:

Assess enterprise AI and automation opportunities from company materials, prioritize up to three testable pilots, and generate evidence-bounded Markdown, HTML, and PDF management reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xixisys](https://clawhub.ai/user/xixisys)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise leaders, operations teams, and consultants use this skill to analyze company materials, identify bounded AI and automation opportunities, and produce management-ready reports for prioritizing pilots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company materials may include personal data, trade secrets, regulated data, customer records, credentials, or production details.

Mitigation: Use redacted or summarized inputs where possible, and avoid submitting credentials or unnecessary sensitive records.

Risk: Generated reports may be incomplete or misleading if reviewed without checking evidence boundaries, assumptions, and fixed contact links.

Mitigation: Review reports before external sharing, confirm evidence gaps, and keep human review for sensitive payment, employment, legal, medical, safety, compliance, account-change, deletion, and bulk-distribution actions.

Risk: PDF output can fail when no compatible browser is available.

Mitigation: Deliver the generated Markdown and HTML, state that PDF generation is incomplete, and rerun the documented command after installing Chrome, Chromium, or Edge.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xixisys/skills/enterprise-ai-opportunity-advisor)
- [Scoring Rubric](references/scoring-rubric.md)
- [Deployment Guidance](references/deployment-guidance.md)
- [Intake Questionnaire](references/intake-questionnaire.md)
- [Report Template](references/report-template.md)
- [Task Taxonomy](references/task-taxonomy.md)
- [Diagnosis Output Schema](schemas/diagnosis-output.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Evidence-bounded analysis, diagnosis JSON, Markdown report, self-contained HTML report, and PDF report when a compatible browser is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local report files; PDF generation requires Chrome, Chromium, or Edge and must not be substituted with HTML.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
