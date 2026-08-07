## Description:

Conspect automates multi-source spreadsheet analysis, chart selection, business report layout, and dashboard or report rendering for presentation-ready outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts, operators, managers, and enterprise IT teams use this skill to turn Excel, CSV, and multi-sheet data into interactive dashboards, offline HTML, static PDF or PNG exports, and structured analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically read uploaded business spreadsheets and analyze every sheet.

Mitigation: Use a dedicated project folder and avoid sensitive spreadsheets unless output locations and retention are controlled.

Risk: The workflow runs bundled local Python tooling and may start a local preview server.

Mitigation: Review the bundled commands and run the skill only in an environment where local tool execution is acceptable.

Risk: The skill persists multiple derived files on disk, including dashboards, reports, and indexes.

Mitigation: Set or inspect output directories before use and remove generated artifacts when they are no longer needed.

Risk: Generated HTML reports may contain business data derived from uploaded spreadsheets.

Mitigation: Review generated HTML before sharing and confirm that only intended aggregate data is present.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/songzhou666/conspect)
- [ClawHub skill page](https://clawhub.ai/songzhou666/skills/conspect)
- [Output specification](artifact/references/output-spec.md)
- [Trigger guide](artifact/references/trigger-guide.md)
- [Quality audit](artifact/references/quality-audit.md)
- [Chart selection](artifact/references/chart-selection.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance and generated files including HTML dashboards, Markdown or HTML reports, PDF, PNG, Word, and JSON indexes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs bundled local Python tooling, may start a local preview server, and writes derived report artifacts to disk.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
