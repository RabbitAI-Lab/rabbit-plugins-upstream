## Description: <br>
Plans multi-origin evacuation routes over raster cost surfaces using 8-connected Dijkstra shortest paths, hazard blockage, and shelter capacity constraints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, emergency planners, and agents use this skill to run local evacuation-routing workflows for synthetic scenarios or local GeoTIFF inputs and inspect generated route, distance, statistics, and manifest files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes credential and network helper modules that are broader than the stated evacuation-routing purpose. <br>
Mitigation: Review the package before installing it in environments with credentials, and prefer a release that removes or clearly documents those helpers. <br>
Risk: Unpinned dependencies can change behavior or introduce supply-chain risk over time. <br>
Mitigation: Pin and review dependencies before deployment, especially for production or credentialed environments. <br>
Risk: Evacuation routes are computed from local or synthetic raster assumptions and may not reflect real-world road access, live hazards, or shelter operations. <br>
Mitigation: Validate inputs, thresholds, shelter capacity assumptions, and outputs with qualified emergency-planning or GIS reviewers before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-emergency-evacuation-routing) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Example output manifest](_test_cli_out/output-manifest.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; runtime artifacts include GeoTIFF, GeoJSON, JSON statistics, and JSON manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally by default; synthetic mode requires no network.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and main script VERSION; openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
