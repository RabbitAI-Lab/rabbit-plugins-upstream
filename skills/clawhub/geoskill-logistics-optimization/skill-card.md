## Description: <br>
VRP/TSP with time windows and capacity constraints to compute optimal routes and cost for logistics <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operations analysts, and logistics teams use this skill to plan local TSP or capacity-constrained VRP routes from GeoJSON customer data or synthetic nodes, then inspect route geometry and cost summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence flags the release as suspicious because the visible route optimizer is mostly local, but the package includes unrelated credential, geocoding, download, and remote-sensing modules that are not clearly disclosed by the skill description. <br>
Mitigation: Review the bundled modules before installing, run the skill in a constrained environment, and remove or audit unrelated modules if only route optimization is needed. <br>
Risk: Bundled helper modules can read user credential files and perform network geocoding or downloads if invoked. <br>
Mitigation: Avoid running the package where sensitive ~/.netrc or ~/.geoskill/secrets.json credentials are present unless those modules have been removed or audited. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-logistics-optimization) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI commands; generated artifacts are JSON and GeoJSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI writes routes.geojson, nodes.geojson, solution.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; CLI VERSION is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
