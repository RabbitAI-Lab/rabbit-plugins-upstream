## Description: <br>
Builds a resistance surface from habitat suitability, identifies ecological corridors with Dijkstra least-cost paths, and computes the PC landscape connectivity index. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and conservation planners use this skill to run local ecological corridor analysis for conservation-redline connectivity, wildlife migration planning, and urban greenway route selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release was flagged suspicious because the package includes under-disclosed credential, network, and home-directory cache utilities alongside an offline corridor tool. <br>
Mitigation: Review before installing, run only the documented corridor CLI in a sandbox, and remove or isolate unused vendored credential and network helpers when possible. <br>
Risk: Vendored helper modules may read ~/.netrc, ~/.geoskill/secrets.json, or unrelated API-key environment variables if they are imported or reused. <br>
Mitigation: Run in an environment without access to user-level credential files or unrelated API-key variables. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-ecological-corridor-design) <br>
- [README](README.md) <br>
- [Skill documentation](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Analysis] <br>
**Output Format:** [GeoTIFF rasters, JSON parameter and manifest files, and optional console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes resistance_surface.tif, corridor.tif, corridor_params.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact script VERSION; artifact changelog and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
