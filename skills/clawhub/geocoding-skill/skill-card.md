## Description: <br>
Forward and reverse geocoding using Nominatim and Open-Meteo, with support for address lookup, coordinate lookup, and batch CSV geocoding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to convert addresses to coordinates, coordinates to addresses, and batches of CSV address data into geocoded outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Addresses, coordinates, and batch CSV values may be sent to Nominatim/OpenStreetMap or Open-Meteo over HTTPS. <br>
Mitigation: Avoid public providers for sensitive customer, employee, facility, or regulated location data unless that sharing is approved; use a self-hosted geocoder for sensitive workloads. <br>
Risk: Some documented advanced flags may not work in the current script. <br>
Mitigation: Test required commands with non-sensitive sample data before using the skill in a production workflow. <br>


## Reference(s): <br>
- [geocoding-skill ClawHub page](https://clawhub.ai/ruiduobao/skills/geocoding-skill) <br>
- [Nominatim](https://nominatim.org/) <br>
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands, Python examples, and CSV/JSON output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local CSV, JSON, state, and map files when the documented commands are run.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
