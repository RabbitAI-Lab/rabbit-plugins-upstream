## Description:

Transform JSON or CSV data into stunning interactive HTML dashboards with auto-detected charts, KPI cards, and dark glass-morphism design. Generates complete standalone HTML with Chart.js.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and operators use this skill to turn JSON, CSV, API responses, metrics, or logs into standalone browser dashboards for reporting, sharing, and monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML embeds the provided raw dataset, which may expose sensitive values if the dashboard is shared.

Mitigation: Use non-sensitive or shareable datasets, or redact the input before generating and distributing the dashboard.

Risk: Generated dashboards load Chart.js from jsDelivr when opened in a browser.

Mitigation: Review or modify the generated HTML for fully offline use when external CDN loading is not acceptable.

## Reference(s):

- [Customization Guide](references/customization.md)
- [Data Type Detection](references/data-types.md)
- [Chart.js](https://chartjs.org)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and generated standalone HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated dashboards embed input data and load Chart.js from jsDelivr unless reviewed or modified for fully offline use.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
