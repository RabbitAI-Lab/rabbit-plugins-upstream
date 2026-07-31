## Description: <br>
Analyze vegetation recovery at mining sites by comparing pre-mining and post-reclamation NDVI rasters and generating recovery statistics and reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and environmental monitoring teams use this skill to assess mine reclamation progress from NDVI raster inputs and produce machine-readable statistics plus a human-readable report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bounding boxes, date ranges, AOI files, and raster inputs may reveal sensitive mining-site or reclamation locations. <br>
Mitigation: Treat location inputs as sensitive data, use approved storage and sharing channels, and prefer local raster workflows when remote data access is not required. <br>
Risk: Unpinned geospatial dependencies can change behavior across environments. <br>
Mitigation: Pin dependency versions, build from a reviewed lockfile, and scan the environment before production use. <br>
Risk: NDVI recovery results can be misleading if rasters are misaligned, low quality, or from unsuitable dates. <br>
Mitigation: Verify raster grid alignment, CRS, nodata handling, and acquisition dates before relying on generated recovery statistics. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-mine-reclamation-monitor) <br>
- [Skill instructions](SKILL.md) <br>
- [Mine reclamation monitor script](scripts/mine_reclamation_monitor.py) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files, JSON, HTML] <br>
**Output Format:** [Markdown guidance with command examples and generated JSON/HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces reclamation-report.json, report.html, and output-manifest.json when the CLI runs successfully.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
