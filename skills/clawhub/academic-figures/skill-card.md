## Description:

Academic Figures helps agents generate publication-ready charts and journal figure assets from JSON or CSV data, including scientific chart types, curated themes, export formats, and PDF quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create publication-ready academic, clinical, and scientific figures, legends, and validation reports from local data files. It is most useful for journal-oriented chart generation where output format, theme selection, font support, and PDF quality checks matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes local utilities beyond chart rendering, including medical lab PDF extraction.

Mitigation: Install only when those utilities are intended, review dependencies first, and run the skill in an isolated virtual environment.

Risk: Processing real medical PDFs may expose sensitive health information, and the security summary flags an overstated de-identification claim.

Mitigation: Do not process real medical PDFs unless privacy, consent, and de-identification requirements have been handled independently.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Data Format Reference](references/data-formats.md)
- [Composite Figure Layout Patterns](references/composite-layouts.md)
- [Clinical Lab Parameter Trend Figure](references/clinical-lab-trends.md)
- [Chinese Hospital Lab Report PDF Extraction](references/chinese-lab-report-extraction.md)
- [Academic Figures Pitfalls](references/pitfalls.md)
- [Examples](examples/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and generated local figure files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide creation of PNG, SVG, PDF, TIFF, EPS, and text legend outputs through bundled local scripts.]

## Skill Version(s):

2.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
