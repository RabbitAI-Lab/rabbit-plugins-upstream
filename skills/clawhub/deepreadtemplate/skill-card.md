## Description:

This skill produces structured deep-read reports for academic papers, organizing the paper into background, variables, paradigm or method, task flow, design details, statistical analysis, and main results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ttggjj](https://clawhub.ai/user/ttggjj)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, graduate students, reviewers, and literature-review writers use this skill to turn an academic paper from a PDF, DOI, arXiv, PubMed link, journal URL, or title into a consistent deep-read report. It is most useful when the user needs comparable notes covering the study background, variables, method, task flow, design details, statistical analysis, main results, and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The report can be incomplete or misleading if the full paper text is unavailable or the source paper omits key details.

Mitigation: Use the skill's missing-data and inference markings, preserve exact paper terminology and numbers, and review the report against the source before relying on it.

Risk: The skill may read or fetch paper files and links supplied by the user.

Mitigation: Provide only paper files or links that are appropriate for the agent environment to access.

Risk: The default report template is mostly Chinese or bilingual, which may not fit every workflow.

Mitigation: Ask explicitly for English-only output when a single-language report is required.

## Reference(s):

- [Literature Deep-Read Report Template](references/deep-read-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown deep-read report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a one-line contribution, seven required analysis sections, and a limitations and reproducibility note; missing or inferred claims are marked.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
