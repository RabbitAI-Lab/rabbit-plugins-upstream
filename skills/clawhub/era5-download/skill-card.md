## Description: <br>
Download ERA5 single-level reanalysis data from Microsoft Planetary Computer without an API key, including temperature, precipitation, wind, pressure, and other climate variables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
Developers, analysts, and climate data users use this skill to search for and download ERA5 single-level reanalysis variables from Microsoft Planetary Computer for specified date ranges and bounding boxes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security review reports unrelated credential helper behavior with embedded Earthdata credentials and local secret-reading behavior in a workflow advertised as no-key public data access. <br>
Mitigation: Review before installation; remove embedded credentials, rotate any exposed accounts, and remove or clearly document credential helpers before broad use. <br>
Risk: The server security review flags undocumented geocoding/cache behavior and unpinned or unlocked dependencies as installation risks. <br>
Mitigation: Install in a controlled environment until geocoding and cache behavior are documented and dependencies are pinned or locked. <br>


## Reference(s): <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/era5-download) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON or file outputs from the CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to run Python CLI commands that search, download, and save ERA5 data files.] <br>

## Skill Version(s): <br>
0.3.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
