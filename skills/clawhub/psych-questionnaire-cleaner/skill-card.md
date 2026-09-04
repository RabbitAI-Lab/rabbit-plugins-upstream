## Description:

Clean, score, and audit psychology questionnaire or survey datasets with reproducible rules, participant-level quality flags, privacy protection, Chinese-language outputs, and traceable reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adecimall](https://clawhub.ai/user/adecimall)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to audit, clean, and score psychology questionnaire or survey datasets while preserving raw data, traceable decisions, and participant-level quality flags. It is intended for data preparation and reporting, not clinical diagnosis or mental-health interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive participant questionnaire data.

Mitigation: Minimize identifiers in reports, avoid row-level sensitive answers in narrative output, preserve raw files unchanged, and use audit records for traceability.

Risk: Predefined response-time and attention-check rules can remove rows from the analytical dataset.

Mitigation: Review the exclusion rules before use, keep excluded rows in a separate record, and report flagged and excluded counts separately.

Risk: Chinese filenames and column names may not fit every downstream workflow.

Mitigation: Confirm that downstream analysts can use Simplified Chinese outputs and provide a reversible original-to-Chinese column-name map.

## Reference(s):

- [Cleaning plan template](artifact/references/cleaning-plan-template.md)
- [Output contract](artifact/references/output-contract.md)
- [Response-quality indicators](artifact/references/quality-indicators.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance, files]

**Output Format:** [Simplified Chinese datasets, audit logs, resolved cleaning plans, quality reports, and unresolved-question summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves raw source data, writes results to a new output directory, separates retained analytical rows from exclusion records, and keeps reversible column-name mappings when fields are renamed.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
