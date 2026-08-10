## Description: <br>
Extracts power lines from LiDAR point clouds, fits catenary sag curves, clusters pylon and tower locations, and computes line-to-tree clearance distances. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial engineers use this skill to analyze local or synthetic LiDAR point clouds for powerline extraction, sag estimation, tower clustering, and line-to-tree clearance reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports under-disclosed credential, geocoding, download, and cache helpers, including hardcoded Earthdata credentials. <br>
Mitigation: Review the package before installation and avoid environments with valuable ~/.netrc entries, ~/.geoskill/secrets.json, or sensitive API keys until those helpers and hardcoded credentials are removed or clearly scoped. <br>
Risk: The documented LiDAR workflow is local, but bundled helper modules are network-capable. <br>
Mitigation: Prefer local input or --synthetic workflows in sensitive environments and inspect or remove unused network/download helpers before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lidar-powerline-detection) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, JSON, Configuration] <br>
**Output Format:** [GeoJSON vector files, JSON reports, run manifests, and concise console status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces powerlines.geojson, towers.geojson, line_tree_distance.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and runtime manifest; artifact CHANGELOG.md and openai.yaml report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
