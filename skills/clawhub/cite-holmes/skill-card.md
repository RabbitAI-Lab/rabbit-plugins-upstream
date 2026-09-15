## Description:

Pkg Cite Holmes Claw guides agents through scoped deep research, iterative search, citation verification, evidence grading, and verified bibliography export for general and medical research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need research reports, fact checks, literature reviews, medical evidence lookups, or reference-list verification with explicit citation status and confidence grading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs broad external lookups and can expose sensitive inputs if used on signed URLs, invitation links, internal URLs, confidential drafts, or patient-related identifiers.

Mitigation: Use it only when external lookups are acceptable, and avoid private, medical, legal, academic, or enterprise research inputs unless review and approval are in place.

Risk: Mechanical citation verification is a helpful signal but does not prove that a source supports a claim, and weak or unverified citations may still need review.

Mitigation: Manually review source support for medical, publication-bound, legal, or high-impact claims before relying on the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](references/search-strategies.md)
- [Report template and reference schema](references/report-template.md)
- [Medical research mode](references/medical-mode.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with citation tables, confidence grades, verification summaries, optional BibTeX, and audit CSV output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke external citation, identifier, archive, and source lookups; offline mode performs structural checks only.]

## Skill Version(s):

1.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
