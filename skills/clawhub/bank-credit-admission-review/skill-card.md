## Description:

This Chinese-language skill helps bank credit and risk-review teams screen underwriting red flags and produce structured credit admission review reports with evidence labels, peer benchmarks, risk ratings, and follow-up due-diligence items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chriskinhaha](https://clawhub.ai/user/chriskinhaha)

### License/Terms of Use:

MIT-0

## Use Case:

Bank credit reviewers, risk managers, and approval support staff use this skill to perform pre-admission red-line screening and full initial credit reviews for enterprise borrowers. It supports Chinese underwriting workflows that combine deterministic checks, source reliability labels, peer benchmarking, working-capital loan sizing, rigid-liability analysis, and documented risk conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger external financial-data lookups and WebSearch for underwriting targets.

Mitigation: Use it only in environments where those lookups are approved, and add an explicit approval step before any third-party query containing borrower or transaction details.

Risk: A direct uploaded-document link appears in the artifact.

Mitigation: Remove or replace the direct link before deployment, and keep sensitive source documents in an approved internal document system.

Risk: Rule-library or benchmark-database updates may persist into later credit decisions.

Mitigation: Review and approve changes to rules, checklists, case logs, and benchmark data before they are reused in future reviews.

Risk: Generated reports could be mistaken for final underwriting decisions.

Mitigation: Require human credit approval, evidence review, and policy checks before acting on any admission, conditional admission, or rejection recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chriskinhaha/skills/bank-credit-admission-review)
- [Admission checklist](references/admission_checklist.md)
- [Negative criteria](references/negative_criteria.md)
- [Data mapping](references/data_mapping.md)
- [Screening report template](references/screening_report_template.md)
- [Analysis framework](references/analysis_framework.md)
- [Data retrieval augmentation](references/data_retrieval_augmentation.md)
- [Source reliability](references/source_reliability.md)
- [Risk rating matrix](references/risk_rating.md)
- [Industry benchmark guide](references/industry_benchmark.md)
- [Working-capital loan demand and rigid-liability analysis](references/loan_demand_analysis.md)
- [Admission standards and control framework](references/admission_standards_control.md)
- [Report template](references/report_template.md)
- [ST risk guide](references/st_risk_guide.md)
- [Rules library](references/rules_library.md)
- [Case log](references/case_log.md)
- [Methodology review template](references/methodology_review.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Chinese Markdown reports with tables, source labels, deterministic script outputs, and optional JSON/script command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory credit-review artifacts and must not replace formal underwriting approval.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
