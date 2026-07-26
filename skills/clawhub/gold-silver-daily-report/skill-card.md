## Description: <br>
Generates an interactive HTML daily market report for gold and silver, covering spot prices, domestic T+D and futures, macro indicators, gold-silver ratio, institutional targets, and bull/bear drivers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tusu168](https://clawhub.ai/user/tusu168) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and market-report authors use this skill to produce a structured daily precious-metals HTML report from current public market data. It is suited for research briefings and internal distribution workflows that need conclusion-first commentary, charts, source-aware data handling, and fixed risk disclosures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated market commentary may be mistaken for investment advice or relied on without checking the underlying data. <br>
Mitigation: Treat the report as research material, review the source data and assumptions, and keep the included disclaimer visible before sharing or acting on the report. <br>
Risk: The workflow depends on public market-data sources whose values, timestamps, or availability can disagree. <br>
Mitigation: Cross-check key prices and macro indicators, remove anomalous or future-dated readings, and note the adopted data cutoff and market session in the report. <br>
Risk: The default rendered report may contact jsDelivr to load ECharts. <br>
Mitigation: For offline or restricted environments, vendor the ECharts asset locally and update the HTML template before generating reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tusu168/skills/gold-silver-daily-report) <br>
- [Data sources and methodology](references/data_sources.md) <br>
- [Report template specification](references/template_spec.md) <br>
- [HTML report template](assets/report_template.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [HTML report file, with optional JSON input data and JavaScript chart snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates a local HTML file named for the report date; the default chart template may load ECharts from jsDelivr unless modified for offline use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
