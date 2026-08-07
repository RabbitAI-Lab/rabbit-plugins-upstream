## Description: <br>
Downloads and subsets global land cover data from ESA WorldCover, FROM-GLC, and GlobeLand30 by region and year with STAC search support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, GIS analysts, and researchers use this skill to search and download global land cover classification data for a selected dataset, year, and WGS84 bounding box. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled credential module may contain exposed Earthdata credentials and under-disclosed secret handling. <br>
Mitigation: Review or remove the credential module before installation and rotate the exposed Earthdata account if it is real. <br>
Risk: Place-name lookup can send location queries to geocoding services and cache lookup data in the user's home directory. <br>
Mitigation: Use explicit --bbox coordinates for privacy-sensitive workflows and review local cache behavior before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-landcover-download) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [Artifact README](artifact/README.md) <br>
- [Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, files, shell commands, guidance] <br>
**Output Format:** [CLI text or JSON output, with downloaded land cover files when download mode is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write data files to the configured output directory and temporary .part files during downloads.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
