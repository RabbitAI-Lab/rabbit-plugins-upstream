## Description: <br>
Models static bathtub flood inundation from DEM data, with optional hydrological connectivity constraints, and produces inundation extent, water depth, and area-volume statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and hydrology practitioners use this skill to run local DEM-based flood screening, compare static and connectivity-constrained inundation methods, and generate GeoTIFF and JSON outputs for downstream review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan verdict is suspicious because the release includes undisclosed credential, network, cache, and vendored-code provenance concerns beyond the local flood CLI workflow. <br>
Mitigation: Review or remove unused bundled core modules before installation and run the documented flood CLI in a restricted local environment. <br>
Risk: The stated flood workflow is local, but hidden network and credential-access capabilities are present in bundled modules that are not necessary for the offline use case. <br>
Mitigation: Use only the documented CLI entrypoint for local DEM or synthetic processing, avoid supplying credentials unless required, and inspect bundled modules before enabling any network-related behavior. <br>


## Reference(s): <br>
- [Skill README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-flood-inundation-modeling) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands, Configuration instructions] <br>
**Output Format:** [GeoTIFF rasters and JSON files, with Markdown usage guidance and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local inundation_mask.tif, water_depth.tif, flood_stats.json, and output-manifest.json outputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata; artifact CLI VERSION agrees; artifact CHANGELOG/openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
