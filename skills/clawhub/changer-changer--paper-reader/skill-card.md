## Description:

Comprehensive PDF paper reader for academic research. Extracts text, figures, tables, and structured content from research papers with support for multimodal analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[changer-changer](https://clawhub.ai/user/changer-changer)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, students, and developers use this skill to extract text, figures, tables, metadata, sections, and references from academic PDF papers. It supports single-paper and folder-based workflows for research review, analysis, and downstream data organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires local Python PDF-processing dependencies before use.

Mitigation: Install dependencies in a virtual environment and review the package set before running extraction workflows.

Risk: Paper extraction workflows can write text, metadata, images, tables, and references into local output folders.

Mitigation: Run the skill in a controlled workspace and inspect output paths before processing sensitive or proprietary papers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/changer-changer/skills/paper-reader)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with bash and Python code blocks; extracted paper artifacts may include TXT, JSON, PNG, CSV, and BibTeX files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may be written into local folders such as paper_output, figures, and tables.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
