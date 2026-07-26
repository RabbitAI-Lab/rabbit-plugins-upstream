## Description: <br>
Builds a multi-element Excel dashboard from CSV or tabular input, with a Dashboard sheet that opens first, formula-driven KPI cards, charts, sparklines, and conditional formatting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iceyliu](https://clawhub.ai/user/iceyliu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and business users use this skill to direct an agent to create an Excel dashboard from CSV or tabular data. It is intended for dashboard-style deliverables with multiple KPIs, charts, sparklines, and conditional formatting rather than simple formatted spreadsheets or financial models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may run a remote OfficeCLI installer without reviewing it first. <br>
Mitigation: Prefer a pinned OfficeCLI release and verify checksums or signatures when available; if using a one-line installer, review the script before execution and run it only in a trusted environment. <br>
Risk: Generated dashboards can be misleading if formulas, cached values, chart ranges, or validation steps are skipped. <br>
Mitigation: Follow the artifact's validation discipline: set calculation behavior, refresh formulas after upstream edits, query expected KPI and chart counts, preview the workbook, and run OfficeCLI validation before delivery. <br>


## Reference(s): <br>
- [OfficeCLI Releases](https://github.com/iOfficeAI/OfficeCLI/releases) <br>
- [OfficeCLI macOS/Linux Installer](https://d.officecli.ai/install.sh) <br>
- [OfficeCLI Windows Installer](https://d.officecli.ai/install.ps1) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with bash and PowerShell commands for producing a single .xlsx dashboard file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OfficeCLI and inherits spreadsheet-engine rules from officecli-xlsx.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
