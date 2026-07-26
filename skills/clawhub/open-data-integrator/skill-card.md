## Description: <br>
Integrate open construction datasets and combine open data sources for enhanced analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, construction analysts, and external project teams use this skill to enrich construction project data with open datasets such as weather, material price indices, labor rates, and permit data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad file and network permissions for construction data analysis. <br>
Mitigation: Install only when file and network access are acceptable, and provide only the project files and provider API keys needed for the specific task. <br>
Risk: Connector outputs may be mistaken for live external data even when the included connector data is demo or sample data. <br>
Mitigation: Treat included connector data as sample data unless live API retrieval is implemented and validated for the task. <br>
Risk: Construction analysis based on incomplete or invalid project inputs can produce misleading summaries or recommendations. <br>
Mitigation: Validate input files and parameters before processing, report errors clearly, and review outputs before using them in project decisions. <br>


## Reference(s): <br>
- [Data Driven Construction](https://datadrivenconstruction.io) <br>
- [OpenWeatherMap API endpoint](https://api.openweathermap.org/data/2.5) <br>
- [ClawHub Skill Page](https://clawhub.ai/datadrivenconstruction/skills/open-data-integrator) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/datadrivenconstruction) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with structured tables and Python code examples when applicable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May offer CSV, Excel, or JSON export guidance when relevant.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata; artifact/claw.json lists 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
