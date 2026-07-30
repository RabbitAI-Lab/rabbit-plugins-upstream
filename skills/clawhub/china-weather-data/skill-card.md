## Description: <br>
Query China meteorological station data from data.cma.cn or Open-Meteo, supporting temperature, precipitation, wind, pressure, humidity, and sunshine output as CSV or JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to query, list, and download China weather records by city, station, or coordinates for analysis and reporting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential-handling code includes a hardcoded Earthdata password and unrelated credential helpers. <br>
Mitigation: Remove the hardcoded credential, rotate any exposed secret, and remove or clearly scope credential helpers that are not needed for China weather queries. <br>
Risk: Location queries may be sent to external geocoding or weather services without full disclosure. <br>
Mitigation: Disclose external location-sharing behavior and avoid sensitive locations unless the operator accepts that data flow. <br>
Risk: Local API key files may expose credentials if stored with permissive filesystem access. <br>
Mitigation: Store API keys with restrictive file permissions and avoid sharing local configuration files. <br>
Risk: Dependency ranges may install vulnerable or incompatible package versions. <br>
Mitigation: Use patched, pinned dependency versions and rescan before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/china-weather-data) <br>
- [China Meteorological Data Service](http://data.cma.cn/) <br>
- [data.cma.cn API documentation](http://data.cma.cn/docDetail/listDoc.html) <br>
- [Open-Meteo](https://open-meteo.com/) <br>
- [Open-Meteo Historical Weather API](https://archive-api.open-meteo.com/v1/archive) <br>
- [Open-Meteo Forecast API](https://api.open-meteo.com/v1/forecast) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Files, Data] <br>
**Output Format:** [Markdown guidance with shell commands; command outputs may be CSV or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a data.cma.cn API key for the CMA source and can fall back to Open-Meteo when no key is configured.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
