## Description: <br>
Query China meteorological station data from data.cma.cn or Open-Meteo, including temperature, precipitation, wind, pressure, humidity, and sunshine data, with CSV or JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data analysts, and agents use this skill to query or download China weather records by city, station ID, coordinates, or province and save the results for analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Location queries, date ranges, and geocoding requests may be sent to external weather or geocoding services, and generated output, QA, or cache files can retain location history. <br>
Mitigation: Use only necessary locations and date ranges, run in a project-specific environment, and inspect or remove generated output, QA, and cache files when location history is sensitive. <br>
Risk: The CMA API key is stored locally in plaintext under the user's home directory. <br>
Mitigation: Avoid configuring a CMA API key unless needed, restrict local file access, use a dedicated key where possible, and rotate or remove the key after use. <br>
Risk: Security evidence says the skill sends some place names to external services more broadly than its privacy text describes. <br>
Mitigation: Review commands before execution, prefer direct coordinates when appropriate, and confirm external-service acceptability for the intended workflow. <br>


## Reference(s): <br>
- [China Meteorological Data Service](http://data.cma.cn/) <br>
- [China Meteorological Data Service API Documentation](http://data.cma.cn/docDetail/listDoc.html) <br>
- [Open-Meteo](https://open-meteo.com/) <br>
- [Open-Meteo Archive API](https://archive-api.open-meteo.com/v1/archive) <br>
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands; CLI output as CSV, JSON, or terminal text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local configuration, weather output files, QA JSON sidecars, and geocoding cache files.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
