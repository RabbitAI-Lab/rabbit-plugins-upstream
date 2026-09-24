## Description:

Bilingual academic writing toolkit for CN/EN style self-checks, deterministic cleanup, integrity-guarded revision support, and disclosure-aware writing-quality review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External scholars, authors, and agents use this skill to review academic or formal drafts for stiff, templated, or machine-flavored writing, then clean mechanical residue and guide quality revisions while preserving facts, citations, numbers, and terminology.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may attempt to use style cleanup to misrepresent authorship, conceal required AI assistance disclosure, or defeat academic-integrity review.

Mitigation: Follow the skill's refusal boundary, preserve required disclosures and provenance labels, and offer only the legitimate writing-quality review path.

Risk: Style scores can be mistaken for authorship, compliance, or external detector results.

Mitigation: Treat scores as local heuristic self-checks only and rely on institutional or journal rules, disclosure, and process evidence for compliance decisions.

Risk: Revisions may accidentally alter numbers, citations, DOIs, PMIDs, years, abbreviations, or required terminology.

Mitigation: Run the included integrity checks after edits and fix the rewrite when verify.py reports a failure.

Risk: Input files outside the supported envelope may produce unreliable or unreadable reports.

Mitigation: Use UTF-8 text, Markdown, or supported docx files, split very long manuscripts by section, and export PDFs to text before processing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Compliance and academic-integrity boundaries](references/compliance.md)
- [End-to-end examples](references/examples.md)
- [FAQ](references/faq.md)
- [English academic style manual](references/style_guide_en.md)
- [Chinese academic style manual](references/style_guide_zh.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain-text reports, optional JSON reports, cleaned text files, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only processing; writes only user-specified output and suggestions paths; supports txt, md, and docx inputs with JSON-capable reports.]

## Skill Version(s):

1.3.0 (source: server release evidence and bundled script version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
