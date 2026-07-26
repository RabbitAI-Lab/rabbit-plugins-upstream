## Description: <br>
Calculate SPI (Standardized Precipitation Index) and SPEI (Standardized Precipitation Evapotranspiration Index) from NASA POWER API data for drought monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and environmental monitoring teams use this skill to calculate SPI/SPEI drought indexes from NASA POWER or local precipitation and water-balance CSV data, classify drought severity, and generate trend reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Loose or unaudited dependency versions can make installations less predictable. <br>
Mitigation: Install in a virtual environment and prefer pinned, audited dependency versions. <br>
Risk: Place-name lookup or geocoding helpers may send location queries outside the local machine and may cache results locally. <br>
Mitigation: Use explicit latitude/longitude or local CSV mode when a clearer privacy boundary is required. <br>
Risk: The skill can write output files to paths selected by the user. <br>
Mitigation: Choose output paths intentionally and review generated files before relying on them. <br>
Risk: Short weather histories can produce unreliable SPI/SPEI distribution fitting, especially for longer timescales. <br>
Mitigation: Use the recommended 20-30 years of monthly data for decisions that depend on index reliability. <br>


## Reference(s): <br>
- [NASA POWER](https://power.larc.nasa.gov/) <br>
- [NASA POWER Daily Point API](https://power.larc.nasa.gov/api/temporal/daily/point) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/drought-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown/text guidance with CLI commands plus CSV, JSON, and NDJSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call NASA POWER or geocoding services depending on command options, and may write local output files selected by the user.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
