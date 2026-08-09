## Description: <br>
Searches and downloads public Sentinel-1 SAR GRD imagery through STAC endpoints, with filters for bounding box, date, polarization, orbit direction, and optional local downloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing practitioners use this skill to generate commands and guidance for finding Sentinel-1 SAR scenes and downloading selected public assets for local analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The inspected artifact documents a downloader but does not include the referenced sentinel1-download.py script. <br>
Mitigation: Review any supplied downloader script separately before installation or execution. <br>
Risk: The requests dependency is specified with a lower bound only, which can reduce install reproducibility. <br>
Mitigation: Pin dependency versions in controlled environments before deployment. <br>
Risk: The skill can download large remote-sensing assets and write them to a local output directory. <br>
Mitigation: Confirm destination paths, available storage, and network use before running download commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/sentinel1-download) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>
- [Element84 Earth Search STAC API](https://earth-search.aws.element84.com/v1/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe network access to public STAC endpoints and local file output paths for downloads.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
