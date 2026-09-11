## Description:

Generates publication-ready academic charts and figure assets from JSON, CSV, or Excel data with journal presets, colorblind-safe themes, accessibility alt text, and local PDF quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, manuscript authors, and technical teams use this skill to choose chart types, prepare input data, and render publication-quality figures for papers, reviews, presentations, and journal submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Python scripts that read selected data files and write figure outputs near the requested path.

Mitigation: Review the command, input path, and output path before execution, and run it only on data files intended for figure generation.

Risk: The environment setup helper may delete the local matplotlib font cache to repair font rendering.

Mitigation: Run setup only in an environment where rebuilding the matplotlib font cache is acceptable.

Risk: Minimum font-size enforcement is not automatic for every rendered output.

Mitigation: Run audit_pdf.py separately when a journal or review process requires a minimum-font-size gate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Data formats reference](references/data-formats.md)
- [Common pitfalls reference](references/pitfalls.md)
- [Composite layouts reference](references/composite-layouts.md)
- [Clinical lab trends reference](references/clinical-lab-trends.md)
- [Color reverse-engineering reference](references/reverse-engineering-colors.md)
- [Examples README](examples/README.md)
- [Scenario templates README](templates/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local figure files such as PNG, SVG, PDF, TIFF, EPS, and alt-text sidecars when commands are executed.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
