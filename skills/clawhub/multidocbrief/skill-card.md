## Description:

Analyzes mixed document sets and produces a source-referenced analytical brief of up to two pages as a Word document.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sergeypetrakov](https://clawhub.ai/user/sergeypetrakov)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing multiple PDFs, Office documents, text files, scans, or images use this skill to synthesize a focused, source-referenced Word brief with a general conclusion and topic-by-topic reasoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted Office, PDF, or image files can expose document-conversion tools to malicious content.

Mitigation: Process only deliberately selected files; use a sandbox for untrusted documents and keep conversion tools and Python dependencies updated.

Risk: Scanned or image-heavy documents may be difficult to read, weakening the brief's conclusions.

Mitigation: Check extraction warnings, inspect relevant images, and verify key figures and source references before sharing the brief.

## Reference(s):

- [ClawHub release](https://clawhub.ai/sergeypetrakov/skills/multidocbrief)
- [Example analysis structure](artifact/references/example_analysis.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Word document]

**Output Format:** [Source-referenced analysis.json and a formatted DOCX brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to two pages; general conclusion, topic summaries, evidence, reasoning, confidence, and source references.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
