## Description:

Finance Audit Agent helps audit teams review insurance, securities, and banking workflows by parsing financial documents, applying 59 audit and compliance rules, and drafting audit reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Audit, compliance, and internal control teams at financial institutions use this skill to triage insurance, securities, banking, AML/KYC, regulatory reporting, and audit remediation tasks. It is intended to support human-reviewed audit work, not replace final professional judgment.

### Deployment Geography for Use:

Global, with regulatory examples focused on China.

## Known Risks and Mitigations:

Risk: The skill may lead an agent to handle sensitive financial documents, customer information, transaction records, AML/KYC materials, and audit reports.

Mitigation: Use it only for explicit finance-audit tasks, provide the minimum necessary data, and redact personal or account identifiers unless the audit environment is authorized for that information.

Risk: AI-generated audit findings or risk labels may be incomplete, outdated, or unsuitable for final regulatory or business decisions.

Mitigation: Require a licensed auditor, compliance owner, or responsible reviewer to confirm final audit conclusions, material findings, and remediation decisions.

Risk: Regulatory references and effective dates may change after the skill release.

Mitigation: Verify cited rules, document numbers, and effective dates against official regulator publications before producing a formal audit report.

Risk: OCR or document extraction can misread low-quality scans, handwritten content, missing pages, or ambiguous fields.

Mitigation: Route low-confidence extraction results and material inconsistencies to manual review before using them as audit evidence.

## Reference(s):

- [ClawHub Finance Audit Agent](https://clawhub.ai/gechengling/skills/finance-audit-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown reports, tabular checklists, and JSON-style structured extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include audit findings, risk ratings, remediation timelines, document extraction fields, regulatory checklists, and human-review prompts.]

## Skill Version(s):

2.0.1 (source: evidence.release.version and artifact version, released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
