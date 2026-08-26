## Description:

Converts academic manuscripts with LaTeX formulas into .docx files with editable Word OMML equations and can optionally produce an image comparison attachment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and academic writers use this skill to convert Markdown or text manuscripts with mathematical notation into editable Word documents for local review and publication workflows. It is especially useful when formulas must remain native OMML objects instead of static images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential screenshots may be exposed if a workflow sends them through cloud OCR.

Mitigation: Use screenshot-based OCR only when the user is comfortable with that data flow, or prefer local text and LaTeX inputs for confidential material.

Risk: Unsupported LaTeX commands or OCR ambiguities can produce degraded formulas or require assumptions.

Mitigation: Review the conversion report, check highlighted fallback formulas in Word or WPS, and confirm any listed transcription assumptions before relying on the document.

Risk: The skill depends on third-party PyPI packages for conversion and optional image rendering.

Mitigation: Review the listed dependencies and their licenses before installation, and install only when math-heavy docx generation is needed.

## Reference(s):

- [Skill README](artifact/README.md)
- [Formula Rules](artifact/references/formula-rules.md)
- [Font Strategy](artifact/references/font-strategy.md)
- [Transcription Guidance](artifact/references/transcription.md)
- [Symbol Table](artifact/references/symbol-table.md)
- [Third-Party Dependencies](artifact/THIRD_PARTY.md)
- [latex2mathml](https://github.com/roniemartinez/latex2mathml)
- [mathml2omml](https://github.com/amedama41/mathml2omml)
- [python-docx](https://github.com/python-openxml/python-docx)
- [matplotlib](https://github.com/matplotlib/matplotlib)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown guidance plus generated .docx files and an optional image comparison .docx attachment]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a conversion report with successful and degraded formula counts; it does not directly generate PDF or PPT output.]

## Skill Version(s):

1.2.1 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
