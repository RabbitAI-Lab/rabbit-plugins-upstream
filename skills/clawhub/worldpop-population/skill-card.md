## Description: <br>
Search and download WorldPop population grid datasets as GeoTIFF files by country, year, and dataset type. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and data teams use this skill to find WorldPop population datasets, inspect available countries and years, and download GeoTIFF grids for spatial demographic analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release was flagged as suspicious because it includes unrelated credential-handling code with hardcoded Earthdata credentials and local secret-file access outside the stated no-key WorldPop workflow. <br>
Mitigation: Install only in an isolated environment, avoid exposing personal .netrc or ~/.geoskill/secrets.json credentials, and review or remove the credential helpers before using this package with sensitive local credentials. <br>


## Reference(s): <br>
- [WorldPop](https://www.worldpop.org/) <br>
- [WorldPop REST API](https://www.worldpop.org/rest/data) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/worldpop-population) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; CLI operations may return JSON and downloaded GeoTIFF files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads can be large; review output paths and dataset size before running download commands.] <br>

## Skill Version(s): <br>
0.3.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
