## Description:

Transforms JSON or CSV data into interactive HTML dashboards with auto-detected charts, KPI cards, a sortable data table, palette options, and Chart.js visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and operators use this skill to turn local JSON or CSV datasets, API responses, metrics, and reports into shareable browser-based dashboards without building a frontend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated dashboards embed the input dataset in an HTML file, which can expose sensitive or confidential data if the file is shared.

Mitigation: Review datasets before conversion and avoid generating dashboards from untrusted or highly confidential data unless sharing and storage controls are understood.

Risk: Generated dashboards load third-party Chart.js code from a CDN when opened in a browser.

Mitigation: Use the skill only in environments where CDN-loaded browser code is acceptable, or review and adapt the generated HTML for local dependency hosting before distribution.

Risk: The skill runs a local Python script against user-selected files.

Mitigation: Install and run it only when local file access by the script is acceptable, and provide only the data files intended for dashboard generation.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/voronindenis5/dashboard-generator)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/dashboard-generator)
- [Chart.js](https://chartjs.org)
- [Customization Guide](references/customization.md)
- [Data Type Detection](references/data-types.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated standalone HTML dashboards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated HTML embeds the selected dataset for browser viewing and loads Chart.js from a CDN.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
