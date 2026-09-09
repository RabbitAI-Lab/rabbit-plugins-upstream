## Description:

Academic Figures helps agents generate publication-ready academic charts and figure assets from JSON or CSV data, with journal presets, local execution, chart-type suggestions, and PDF verification gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, analysts, and writing agents use this skill to turn structured study or analysis data into publication-oriented figures, legends, and validation commands. It is suited for local chart generation workflows where source data should remain on the user's machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency or environment changes can affect reproducibility of generated figures.

Mitigation: Install the skill in an isolated virtual environment and pin dependency versions when repeatable outputs matter.

Risk: The setup helper may clear the matplotlib font cache while preparing CJK font support.

Mitigation: Run setup_env.py only in environments where that cache cleanup is acceptable.

Risk: Reference material discusses scraping content from JavaScript-rendered pages.

Mitigation: Use that note only for content the user is authorized to download or analyze.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Data Format Reference](references/data-formats.md)
- [Composite Figure Layout Patterns](references/composite-layouts.md)
- [Academic Figures - Pitfalls](references/pitfalls.md)
- [Clinical Lab Parameter Trend Figure](references/clinical-lab-trends.md)
- [Reverse-Engineering Chart Colors from Reference Images](references/reverse-engineering-colors.md)
- [academic-figures v1.5.0 Upgrade Analysis](references/v1.5-upgrade-analysis.md)
- [Examples README](examples/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline bash commands; generated assets may be PNG, SVG, PDF, TIFF, EPS, or TXT when commands are run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against user-provided JSON or CSV data and can emit verification exit codes for rendered PDFs.]

## Skill Version(s):

2.1.0 (source: frontmatter and server release evidence, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
