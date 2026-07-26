## Description: <br>
Calculate solar photovoltaic energy potential from NASA POWER solar radiation data, including annual GHI, optimal tilt, estimated PV output, and basic economic metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and energy planners use this skill to estimate site-level or batch solar PV potential from coordinates or resolved place names and to generate JSON outputs for feasibility screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Coordinates are sent to NASA POWER, and natural-language place names may be sent to Open-Meteo or Nominatim and cached locally. <br>
Mitigation: Use exact latitude and longitude for sensitive locations, disable Nominatim where appropriate, and avoid submitting sensitive place names. <br>
Risk: Runtime dependencies include requests and numpy, which should remain current for secure use. <br>
Mitigation: Install with a locked dependency set that uses patched versions of requests and numpy. <br>
Risk: Solar output and economic results are estimates based on simplified assumptions and public weather data resolution. <br>
Mitigation: Use the generated results for feasibility screening and validate final system designs with engineering-grade tools and local site data. <br>


## Reference(s): <br>
- [NASA POWER API endpoint](https://power.larc.nasa.gov/api/temporal/daily/point) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/solar-energy-potential) <br>
- [details.md](references/details.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, CSV, Shell commands, Guidance] <br>
**Output Format:** [Command-line text with optional JSON or CSV result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write a JSON QA sidecar when requested with --qa.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
