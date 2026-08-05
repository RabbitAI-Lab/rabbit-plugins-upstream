## Description: <br>
Download ERA5 single-level climate data from Microsoft Planetary Computer without an API key, supporting multiple variables and spatial subsetting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, data scientists, and geospatial analysts use this skill to guide an agent through searching for and downloading ERA5 climate reanalysis data from Microsoft Planetary Computer, including variable selection, date ranges, spatial bounding boxes, and NetCDF output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill declares minimum dependency versions rather than a locked environment, which can leave installations exposed to dependency drift or known package issues. <br>
Mitigation: Pin or update dependencies before use and run an environment-level dependency audit as recommended by the ClawHub security guidance. <br>
Risk: Using the skill can trigger outbound HTTPS requests and write climate data files to the chosen output path. <br>
Mitigation: Run it in an environment where public-network access and local output paths are approved, and review the selected output directory before large downloads. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-era5-download) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide outbound HTTPS requests to public data sources and local climate-data file writes to the selected output path.] <br>

## Skill Version(s): <br>
4.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
