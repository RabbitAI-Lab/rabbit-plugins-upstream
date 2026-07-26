## Description: <br>
Download NASA POWER meteorological and solar energy data, including solar radiation, temperature, precipitation, wind speed, humidity, and other parameters for point or regional queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and researchers use this skill to generate commands and guidance for downloading NASA POWER weather and solar resource datasets for energy, agriculture, hydrology, and climate workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Place-name searches can disclose the searched location to third-party geocoding services. <br>
Mitigation: Use explicit latitude/longitude or bounding boxes instead of --place when locations are sensitive. <br>
Risk: The skill downloads requested NASA data to local output files. <br>
Mitigation: Choose output paths intentionally, review generated files before sharing, and remove sensitive derived datasets when no longer needed. <br>
Risk: Runtime behavior depends on external Python packages such as requests and tqdm. <br>
Mitigation: Pin and update dependencies in controlled environments before operational use. <br>


## Reference(s): <br>
- [NASA POWER API](https://power.larc.nasa.gov/api/) <br>
- [NASA POWER Documentation](https://power.larc.nasa.gov/docs/) <br>
- [NASA POWER Parameters](https://power.larc.nasa.gov/docs/v1/parameters/) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/nasa-power-download) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance, configuration, code] <br>
**Output Format:** [Markdown guidance with shell commands; commands can write CSV, JSON, and QA JSON data files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The generated workflow can call NASA POWER and, when --place is used, a geocoding service; downloaded data is written to local output paths.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
