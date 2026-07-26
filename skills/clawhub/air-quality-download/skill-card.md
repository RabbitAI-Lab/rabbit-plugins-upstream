## Description: <br>
Download air quality data (PM2.5, PM10, O3, NO2, SO2, CO) from Open-Meteo Air Quality API (free, no key). Supports current, historical, and forecast data with hourly/daily/monthly aggregation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data practitioners use this skill to generate commands and run a Python downloader for current, historical, or forecast air quality data. It supports location-based pollutant retrieval, aggregation, and CSV or JSON outputs for analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Location privacy may be affected when place-name inputs are geocoded or cached locally. <br>
Mitigation: Prefer explicit latitude and longitude inputs for sensitive locations, and document or disable the home-directory geocoding cache before deployment. <br>
Risk: The WAQI token path is present but not clearly documented in the main skill instructions. <br>
Mitigation: Avoid using or extending WAQI token behavior until token handling, endpoint behavior, and user disclosure are documented. <br>
Risk: Dependency constraints are broad for the requests package. <br>
Mitigation: Tighten and review dependency versions before installing in controlled or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/air-quality-download) <br>
- [Open-Meteo Air Quality API](https://open-meteo.com/en/docs/air-quality-api) <br>
- [Open-Meteo](https://open-meteo.com/) <br>
- [WAQI API](https://api.waqi.info/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; generated CSV or JSON data files when the downloader is run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include current, historical, forecast, and QA summary files depending on command options.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
