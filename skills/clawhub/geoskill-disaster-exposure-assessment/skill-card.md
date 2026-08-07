## Description: <br>
Overlays hazard zones with asset and population spatial data to quantify exposure by raster zones and vector point-in-polygon joins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS analysts use this skill to run local disaster-exposure calculations for a bounding box or multi-band GeoTIFF and produce exposure masks, hazard-zone boundaries, and exposure statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server security review marks the package suspicious because it includes network, downloader, cache, and credential-handling support code beyond the advertised local disaster-exposure CLI. <br>
Mitigation: Run the skill in an isolated environment, review or remove unused support modules before deployment, and limit credentials available to the process. <br>
Risk: The server security guidance recommends dependency pinning before production use. <br>
Mitigation: Pin geospatial dependencies, rebuild the environment from those pins, and rerun the included CLI and core tests before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-disaster-exposure-assessment) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [License](LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF, GeoJSON, JSON, and run manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally by default and writes an output manifest with inputs, outputs, and QA summary.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
