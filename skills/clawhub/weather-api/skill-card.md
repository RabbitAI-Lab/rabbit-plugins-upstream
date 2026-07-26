## Description: <br>
Fetch weather data for construction scheduling, including historical data, forecasts, and outdoor work risk assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction project teams and developers use this skill to fetch Open-Meteo weather forecasts or historical data for job sites and assess weather-related schedule risk for outdoor activities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts Open-Meteo with site coordinates, which can reveal sensitive project locations. <br>
Mitigation: Use only the location precision needed for the analysis and avoid sharing sensitive exact coordinates unless required. <br>
Risk: The skill may read or export user-provided project files during analysis. <br>
Mitigation: Provide only relevant project files and review any CSV, Excel, or JSON export before sharing it outside the project team. <br>
Risk: Weather-based schedule recommendations can be wrong or incomplete if inputs are inaccurate or local operating constraints are missing. <br>
Mitigation: Validate site coordinates, dates, activities, and risk thresholds before relying on the output for construction scheduling decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/weather-api) <br>
- [Publisher homepage](https://datadrivenconstruction.io) <br>
- [Open-Meteo API](https://open-meteo.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with structured tables, summary findings, and optional Python-oriented examples or export guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include weather condition tables, risk levels, workable-hour estimates, affected activities, recommendations, and CSV/Excel/JSON export suggestions.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
