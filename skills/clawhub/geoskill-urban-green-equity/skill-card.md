## Description: <br>
Assess urban green space distribution equity across populations and communities using quantity, quality, and walkable accessibility metrics to identify service gaps and priority intervention areas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Urban planners, geospatial analysts, and civic-data teams use this skill to assess neighborhood green-space access, compare equity metrics, and identify priority communities or candidate interventions. It expects local geospatial inputs such as parks or green-space polygons, a walkable road network, and community boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dependency hygiene issues could affect reproducibility or introduce unwanted package changes. <br>
Mitigation: Install in an isolated environment and pin or review dependencies before production use. <br>
Risk: The skill writes analysis outputs to disk during normal operation. <br>
Mitigation: Provide an explicit output directory and review generated files before sharing or using them in downstream workflows. <br>
Risk: The documented auto-download/cache mode does not fully match the script behavior. <br>
Mitigation: Treat auto-download and cache workflows cautiously; prefer explicit local input files unless the release is reviewed and tested for that mode. <br>


## Reference(s): <br>
- [Equity factors and thresholds](references/equity_factors.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-urban-green-equity) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI commands and generated GeoJSON, CSV, and JSON analysis files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces green service areas, community metrics, equity summaries, priority communities, request and dataset manifests, output metadata, and QA reports in a user-selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
