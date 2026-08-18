## Description:

Transform CSV data into stunning interactive chart visualizations with Chart.js.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to inspect CSV files and generate interactive HTML charts or dashboards with automatic chart selection, palettes, trend lines, theme toggling, and PNG export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports run browser JavaScript and load Chart.js from a third-party CDN.

Mitigation: Open generated reports only in environments where third-party network requests are allowed, or bundle Chart.js locally with appropriate integrity and content security protections.

Risk: Some CSV-derived text is not safely escaped in generated HTML.

Mitigation: Use trusted CSV inputs or add HTML escaping and sanitization before generating reports.

Risk: Generated reports may expose sensitive CSV data when opened or shared.

Mitigation: Avoid opening or distributing generated HTML reports containing sensitive data unless the operating environment and sharing path are approved.

## Reference(s):

- [Chart Selection Guide](references/chart-selection.md)
- [Color Palette Guide](references/palettes.md)
- [Server-Resolved Source Repository](https://github.com/voronindenis5/data-viz-wizard)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/data-viz-wizard)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and generated HTML/JavaScript visualization files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports are active browser HTML that load Chart.js from a third-party CDN.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
