## Description: <br>
Get current weather and forecasts from MeteoSwiss (official Swiss weather service). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xenofex7](https://clawhub.ai/user/xenofex7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to retrieve Switzerland-specific current weather measurements from MeteoSwiss stations and multi-day forecasts by Swiss postal code. <br>

### Deployment Geography for Use: <br>
Global; weather data coverage is Switzerland. <br>

## Known Risks and Mitigations: <br>
Risk: Forecast queries send the requested Swiss postal code to MeteoSwiss. <br>
Mitigation: Avoid using postal codes that reveal sensitive personal location context, or use station-based current weather lookups when a postal-code forecast is not needed. <br>
Risk: Optional Python scripts depend on the requests package and execute local network calls. <br>
Mitigation: Run the scripts in a trusted Python environment and review dependencies before deployment. <br>
Risk: The forecast endpoint is documented as occasionally unstable or subject to change. <br>
Mitigation: Fall back to the public current-weather CSV endpoint when forecast requests fail. <br>


## Reference(s): <br>
- [MeteoSwiss API Reference](references/api_info.md) <br>
- [Official MeteoSwiss](https://www.meteoschweiz.admin.ch) <br>
- [Swiss Open Government Data Platform](https://data.geo.admin.ch) <br>
- [Current Weather Measurements CSV](https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv) <br>
- [ClawHub Skill Page](https://clawhub.ai/xenofex7/skills/swissweather) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts can return formatted text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No API key is required; optional Python scripts require requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
