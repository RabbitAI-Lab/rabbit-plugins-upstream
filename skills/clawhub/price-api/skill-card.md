## Description: <br>
Fetch construction material prices from open APIs. Track price trends, regional variations, and update cost databases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, estimators, and construction cost teams use this skill to fetch public material price data, analyze price trends and regional variation, and prepare cost database updates for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cost database updates may introduce incorrect prices or assumptions if applied without review. <br>
Mitigation: Review proposed updates, summary statistics, and changed fields before applying or exporting revised cost data. <br>
Risk: Shared project files may expose sensitive API credentials if keys are hard-coded. <br>
Mitigation: Keep API keys out of shared files and use environment-specific secret handling where credentials are needed. <br>
Risk: Current market data, estimates, and regional factors may be incomplete or stale for a specific project context. <br>
Mitigation: Validate inputs and compare generated estimates against project-specific sources and construction cost standards before use. <br>


## Reference(s): <br>
- [Price Api on ClawHub](https://clawhub.ai/datadrivenconstruction/skills/price-api) <br>
- [datadrivenconstruction profile](https://clawhub.ai/user/datadrivenconstruction) <br>
- [datadrivenconstruction homepage](https://datadrivenconstruction.io) <br>
- [FRED API documentation](https://fred.stlouisfed.org/docs/api/) <br>
- [FRED observations API endpoint](https://api.stlouisfed.org/fred/series/observations) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured tables, summary statistics, key findings, and optional export guidance for CSV, Excel, or JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose updates to user-provided cost data; users should review changes before applying or exporting them.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
