## Description: <br>
Multi-criteria screening of groundwater recharge potential using terrain, soil, geology, land cover, drainage density, rainfall, AHP, weighted overlay, fuzzy aggregation, sensitivity analysis, and spatial validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to identify higher-potential groundwater recharge zones, compare weighting scenarios, and generate candidate recharge area maps for planning review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Groundwater recharge maps may be misread as authoritative engineering, legal, or well-success determinations. <br>
Mitigation: Treat outputs as planning-screening evidence only and require hydrogeological field review, administrative review, and legal compliance checks before decisions. <br>
Risk: Results depend on local raster availability, factor scoring, weights, and dependency versions. <br>
Mitigation: Run in a project or virtual environment, review dependency versions when reproducibility matters, confirm required local raster inputs, and record factor configuration and weights with each run. <br>


## Reference(s): <br>
- [Default Recharge Factors](references/recharge_factors.json) <br>
- [ClawHub Release Page](https://clawhub.ai/ruiduobao/skills/geoskill-groundwater-recharge-potential) <br>
- [Publisher Profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown text with bash commands plus local geospatial outputs such as GeoTIFF, GeoJSON, JSON manifests, report text, QA records, and logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces planning-screening outputs including recharge_potential.tif, candidate_zones.geojson, factor_weights.json, sensitivity.json, request and output manifests, qa.json, report.pdf, and run.log.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
