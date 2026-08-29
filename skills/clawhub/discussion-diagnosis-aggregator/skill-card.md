## Description:

Aggregate 6 single-skill diagnosis outputs into one Discussion report with scoring, severity tags, and top-3 priorities, delivered as a chat reply in the conversation language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[laninga](https://clawhub.ai/user/laninga)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, instructors, and writing-support agents use this skill to combine six prior Discussion-section diagnoses into one self-contained academic writing report. It deduplicates overlapping issues, assigns severity, prioritizes fixes, calculates weighted scores, and anchors recommendations with examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The final report may inherit incorrect or inconsistent findings from the six input diagnosis outputs.

Mitigation: Review the source diagnosis blocks and the aggregated severity, score, and priority decisions before relying on the report.

Risk: Temporary processing files may be created when the agent handles documents during diagnosis.

Mitigation: Use an appropriate workspace for document processing and request exported Markdown only when a report file is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/laninga/skills/discussion-diagnosis-aggregator)
- [Output template](references/output-template.md)
- [Severity rubric](references/severity-rubric.md)
- [Cross-dimension map](references/cross-dimension-map.md)
- [Good Midgley 2020 full diagnosis example](references/examples/good_midgley_2020_full_diagnosis.md)
- [Mixed synthetic partial issues example](references/examples/mixed_synthetic_partial_issues.md)
- [Bad synthetic full diagnosis example](references/examples/bad_synthetic_full_diagnosis.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown chat report in the conversation language; Markdown file only when the user explicitly requests export.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aggregates six prior diagnosis outputs into weighted scores, severity-tagged issues, top-3 fixes, deduplication notes, and strengths.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
