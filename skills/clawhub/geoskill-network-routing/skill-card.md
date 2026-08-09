## Description: <br>
Dijkstra/A* multi-constraint path planning with support for time or distance weights and multiple origins and destinations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run local network routing workflows over synthetic or local input data, producing route geometries, routing statistics, and a run manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes helper modules that can contact external services, download URLs, cache results, and read local credential stores, even though the main routing command is described as local. <br>
Mitigation: Audit or remove unused helper modules before installation, pin dependencies, and run the routing command only with trusted local inputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-network-routing) <br>
- [README](README.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Configuration, Shell commands, Guidance] <br>
**Output Format:** [GeoJSON routes, JSON routing statistics, JSON manifest, and markdown or shell-command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The routing command writes local output files such as routes.geojson, routing_stats.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
