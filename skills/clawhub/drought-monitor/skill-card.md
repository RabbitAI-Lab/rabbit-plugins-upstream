## Description: <br>
Calculates SPI and SPEI drought indices from NASA POWER precipitation data or local CSV inputs, with drought classification and trend-report outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, climate analysts, and geospatial teams use this skill to fetch or process precipitation and water-balance data, then generate SPI/SPEI drought classifications, time-series files, and trend summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential-handling code includes a hardcoded Earthdata password and helpers that read local credential files. <br>
Mitigation: Review or remove the credential module before installation, rotate any exposed credentials, and run the skill in an isolated environment with only intended credentials available. <br>
Risk: Place-name geocoding and NASA POWER requests can disclose queried locations, coordinates, dates, and parameter selections to external services. <br>
Mitigation: Use local CSV mode or explicit non-sensitive coordinates for sensitive work, and avoid place-name geocoding unless external lookup is acceptable. <br>
Risk: Dependency versions are specified as minimums, so unreviewed newer packages could change behavior. <br>
Mitigation: Pin dependency versions after review and install in a dedicated environment before operational use. <br>


## Reference(s): <br>
- [NASA POWER Project](https://power.larc.nasa.gov/) <br>
- [CHIRPS Data](https://www.chc.ucsb.edu/data/chirps) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and Python command examples; the bundled CLI writes CSV, JSON, and NDJSON data files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [SPI/SPEI outputs include date, index value, and drought classification; report output includes JSON summary statistics, drought frequency, and trend direction.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
