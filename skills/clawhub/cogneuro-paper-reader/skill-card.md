## Description:

Reads and summarizes cognitive neuroscience and experimental psychology research papers (PDF or plain text) on attention, working memory, sustained attention, memory, decision-making, and neural population coding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guigui855](https://clawhub.ai/user/guigui855)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, students, and analysts use this skill to turn provided cognitive neuroscience or experimental psychology papers into structured summaries with hypotheses, methods, statistics, results, limitations, glossary terms, and critical-reading notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF text extraction may fail or omit content, especially for scanned PDFs.

Mitigation: If extracted text is empty or incomplete, ask for OCR or source text and avoid fabricating missing content.

Risk: Structured summaries may be lengthy or contain copied statistics that need verification.

Mitigation: Review the citation, statistics, effect sizes, and not-reported fields against the provided paper before relying on the summary.

## Reference(s):

- [Domain Glossary - Attention, Memory, & Population Neuroscience](references/domain-glossary.md)
- [Statistics Guide - Reading the Numbers in These Papers](references/statistics-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown structured summary, optionally with inline shell commands for local PDF text extraction]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes exact reported values, marks omitted information as not reported, and includes critical-reading notes.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
