## Description:

Academic writing revision advisor for the Results section of psychology and STEMM research papers. Checks claim-hedging alignment, causal language appropriateness, statistical reporting completeness, and interpretation boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seulkilu](https://clawhub.ai/user/seulkilu)

### License/Terms of Use:

MIT-0

## Use Case:

Academic authors, reviewers, and editing agents use this skill to audit Results-section drafts for claim strength, hedging, causal language, interpretation boundaries, and subjective phrasing. It produces sentence-level scores and revision suggestions grounded in curated psychology-paper examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be mistaken for a full statistical-analysis validator.

Mitigation: Use it to review reporting language and claim strength only; verify statistical methods, assumptions, tests, and results separately.

Risk: Causal-language findings may be overly conservative when the study design is not supplied.

Mitigation: Provide the research design before relying on causal-language scores or treat flagged causal terms as review prompts.

Risk: The artifact requires Chinese-style scoring labels and headings, which may not match every English-language workflow.

Mitigation: Confirm the target output language and heading requirements before using the report directly in an editing pipeline.

## Reference(s):

- [Scoring Rubric](references/rubric.md)
- [Diagnostic Checklist](references/checklist.md)
- [Curated Psychology Examples](references/examples/examples_memberF.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown audit report with standardized headings, dimension scores, evidence excerpts, example comparisons, revision suggestions, and priority levels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses 1-5 scoring across five dimensions and may require the research design to improve causal-language judgments.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
