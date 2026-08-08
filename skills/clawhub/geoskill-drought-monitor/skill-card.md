## Description: <br>
Calculate SPI and SPEI drought indices from NASA POWER precipitation data with multi-timescale support, drought classification, and trend analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to calculate drought indices, classify drought conditions, and generate trend reports from NASA POWER data or local CSV weather data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: NASA POWER queries send latitude, longitude, date range, and parameter selections to an external service. <br>
Mitigation: Use local CSV mode for sensitive locations or date ranges. <br>
Risk: Dependency versions are lower-bounded rather than pinned. <br>
Mitigation: Pin or constrain dependency versions before production deployment. <br>
Risk: Short climate records can produce unreliable SPI or SPEI distribution fitting. <br>
Mitigation: Prefer 20 to 30 years of monthly data and review drought-index outputs before operational decisions. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/ruiduobao/skills/geoskill-drought-monitor) <br>
- [NASA POWER Project](https://power.larc.nasa.gov/) <br>
- [NASA POWER Daily Point API](https://power.larc.nasa.gov/api/temporal/daily/point) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated tool outputs can be CSV, JSON, or NDJSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports SPI, SPEI, and report workflows with optional local CSV processing.] <br>

## Skill Version(s): <br>
4.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
