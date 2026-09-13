## Description:

Checks submitted reference lists against GB/T 7714—2025 bibliographic formatting rules and returns a structured report of errors, warnings, uncertain items, and suggested corrected entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[libv70](https://clawhub.ai/user/libv70)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, editors, students, and research support staff use this skill to review reference lists and manuscript reference sections for GB/T 7714—2025 formatting issues. It helps identify missing elements, incorrect type markers, punctuation problems, old-standard patterns, and consistency issues between in-text citations and the bibliography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may provide references or manuscript excerpts they do not want an agent to inspect.

Mitigation: Provide only reference lists or documents that are appropriate for agent review.

Risk: The skill output is formatting guidance and is not the official GB/T 7714—2025 standard text.

Mitigation: Verify uncertain or high-stakes formatting decisions against the official standard text or the target journal, institution, or publisher requirements.

Risk: Corrected reference examples could mislead users if missing bibliographic facts are filled in as if they were known.

Mitigation: Use visible placeholders for missing facts and require the user to supply real dates, DOI values, patent numbers, URLs, or other bibliographic details.

## Reference(s):

- [GB/T 7714—2025 rules summary](artifact/references/gbt7714-2025-rules.md)
- [National Public Service Platform for Standards Information](https://openstd.samr.gov.cn)
- [ClawHub skill page](https://clawhub.ai/libv70/skills/gbt7714-reference-checker)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown structured reference-checking report with status tables and corrected-entry suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses placeholders for missing bibliographic facts and marks unresolved rules or unsupported cases as uncertain.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; source skill frontmatter reports 3.0.0-public)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
