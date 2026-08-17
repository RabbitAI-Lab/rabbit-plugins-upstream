## Description:

mddoc converts Markdown files or pasted Markdown into academically formatted Word (.docx) documents with structured headings, body text, tables, images, page headers, and LaTeX-style math.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trisia](https://clawhub.ai/user/trisia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, students, researchers, and technical writers use this skill to turn Markdown source material into Word documents that follow a Chinese academic formatting profile. It is most relevant for papers, reports, theses, and other documents requiring strict heading, table, image, header, and math formatting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup workflow can create a reusable Python virtual environment and install dependencies from the network.

Mitigation: Run setup in an approved environment and review dependency installation policy before deployment.

Risk: Markdown documents with remote image URLs can trigger outbound requests during conversion.

Mitigation: For sensitive or untrusted documents, remove remote image URLs or pre-download approved images before conversion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/trisia/skills/mddoc)
- [Evaluation manifest](artifact/evals/evals.json)
- [LaTeX coverage evaluation document](artifact/evals/test-latex-coverage.md)
- [Sample Markdown evaluation document](artifact/evals/test-sample.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [DOCX file plus Markdown instructions and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or reuses a dedicated Python virtual environment and may fetch remote images referenced by the input Markdown.]

## Skill Version(s):

0.1.9 (source: server release evidence and target metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
