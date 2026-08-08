## Description: <br>
Performs local spatial joins between vector layers using spatial relationship predicates and attribute aggregation statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run offline spatial joins on local or synthetic vector data and summarize joined attributes by zone. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes network, downloader, cache, and credential-handling modules that are not disclosed by the offline spatial-join description. <br>
Mitigation: Review the package before installation and reduce it to the spatial-join entrypoint, or remove and clearly gate the extra modules before use. <br>
Risk: Credential and .netrc handling may be inappropriate in environments that must isolate local secrets. <br>
Mitigation: Do not install in sensitive environments unless credentials and local secret stores are isolated from this package. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-spatial-join-analysis) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, json, text] <br>
**Output Format:** [GeoJSON and JSON files with optional CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes spatial_join.geojson, join_stats.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
