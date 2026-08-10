## Description: <br>
Classifies climate zones from monthly temperature and precipitation rasters using Koepen-Geiger or simplified Strahler schemes, with area statistics and optional change detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and climate researchers use this skill to classify local 24-band climate rasters or synthetic climate fields into climate-zone classes, summarize area by class, and compare two epochs for zone changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes location lookup, downloader, and credential modules beyond the advertised local climate-classification workflow. <br>
Mitigation: Review or remove those modules before installation or deployment, and limit use to the reviewed climate-classification entrypoint. <br>
Risk: The security evidence treats a hardcoded Earthdata credential as exposed. <br>
Mitigation: Do not use packaged credentials; rotate or revoke any affected credential before running the package in a trusted environment. <br>
Risk: Undisclosed network access or home-directory credential reads may be unacceptable in controlled environments. <br>
Mitigation: Run with network egress and home-directory credential access blocked unless those behaviors have been explicitly reviewed and approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-climate-zone-classification) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with Python CLI commands; generated skill outputs include GeoTIFF, JSON area statistics, and JSON manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local files named climate_zones.tif, area_statistics.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; script VERSION agrees, artifact CHANGELOG lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
