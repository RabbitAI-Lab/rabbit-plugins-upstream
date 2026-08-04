## Description: <br>
Download current, historical, and forecast air quality data for PM2.5, PM10, ozone, nitrogen dioxide, sulphur dioxide, and carbon monoxide from Open-Meteo without requiring an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data analysts, and environmental workflows use this skill to retrieve air quality time series or forecasts for selected coordinates and pollutants, then save the results for analysis or automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Some advanced examples in the skill documentation do not match the actual script command surface. <br>
Mitigation: Prefer the implemented current, historical, and forecast commands and verify arguments with the script help before using examples in automation. <br>
Risk: Place-name lookup sends the place query to OpenStreetMap Nominatim. <br>
Mitigation: Use explicit latitude and longitude when place names are sensitive or should not be sent to a geocoding service. <br>
Risk: Downloader requests send coordinates, dates, and pollutant selections to external air-quality services. <br>
Mitigation: Review the selected data source and avoid submitting sensitive location patterns when that disclosure is not acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-air-quality-download) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [Open-Meteo Air Quality API documentation](https://open-meteo.com/en/docs/air-quality-api) <br>
- [Open-Meteo](https://open-meteo.com/) <br>
- [WAQI token registration](https://aqicn.org/data-platform/token/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated downloader outputs are CSV or JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call Open-Meteo, OpenStreetMap Nominatim for place lookup, or WAQI when that mode is used.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
