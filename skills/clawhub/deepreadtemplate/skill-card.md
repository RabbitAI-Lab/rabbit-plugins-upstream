## Description:

Deep Read Template helps an agent turn an academic paper from a PDF, DOI, arXiv link, or title into a structured deep-read literature report with exact-number extraction, visual method diagrams, and research implications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ttggjj](https://clawhub.ai/user/ttggjj)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, graduate students, reviewers, and literature-review workflows use this skill to extract a paper's background, variables, methods, design details, statistical analysis, results, limitations, and implications into reusable notes and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read provided PDFs or search for and download public paper copies.

Mitigation: Use papers you are allowed to process, and avoid private manuscripts unless the user is comfortable having the agent process them for report generation.

Risk: A paywalled or unavailable full text can lead to an abstract-based report with less complete evidence.

Mitigation: Clearly mark when full text was not obtained and state which public sources or paper sections were used.

Risk: Extracted statistics, sample sizes, or effect estimates can mislead downstream research if copied incorrectly.

Mitigation: Quote exact numbers from the original paper and verify important values against the source before relying on the report.

## Reference(s):

- [Literature Deep-Read Report Template & Extraction Prompts](references/deep-read-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code]

**Output Format:** [Markdown report and self-contained HTML document]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an inline SVG mechanism or method diagram and avoids external libraries in the HTML report.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
