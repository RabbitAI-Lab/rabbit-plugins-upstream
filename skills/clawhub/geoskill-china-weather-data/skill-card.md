## Description: <br>
Query China meteorological station data by city, station, or coordinates using data.cma.cn or Open-Meteo, with CSV, JSON, and station-list outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to query or download China weather station and gridded weather data for temperature, precipitation, wind, pressure, humidity, and sunshine workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Weather locations, place names, and date ranges may be sent to external weather services. <br>
Mitigation: Use only locations and date ranges appropriate to share with the selected provider, and review provider terms before operational use. <br>
Risk: A data.cma.cn API key may be stored in a local plaintext configuration file. <br>
Mitigation: Prefer environment-based secrets where practical, restrict local config file access, and remove saved keys when no longer needed. <br>
Risk: Downloaded CSV files and optional QA summaries are written to user-selected paths. <br>
Mitigation: Write outputs only to trusted project paths and review generated files before sharing or ingesting them downstream. <br>
Risk: The release depends on external Python packages and external provider endpoints. <br>
Mitigation: Use pinned and updated dependencies, and prefer encrypted provider endpoints where available. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-china-weather-data) <br>
- [China Meteorological Data Service](http://data.cma.cn/) <br>
- [Open-Meteo](https://open-meteo.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, files, shell commands, configuration] <br>
**Output Format:** [Plain text tables, JSON records, CSV files, and local JSON configuration or QA sidecar files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires date ranges and a city, station, or coordinates; data.cma.cn access may require a user-provided API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
