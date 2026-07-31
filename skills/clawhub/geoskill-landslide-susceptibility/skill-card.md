## Description: <br>
Integrates terrain, geology, rainfall, land cover, roads, and historical landslide data to produce interpretable susceptibility zoning with spatial cross-validation. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External analysts, developers, and geospatial engineers use this skill to generate landslide susceptibility maps, compare model choices, inspect factor importance, and produce spatial cross-validation artifacts for a region. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outputs may be mistaken for production landslide hazard or risk assessments even when the pipeline relies on synthetic predictor data. <br>
Mitigation: Clearly label synthetic and demo outputs, require validated real factor rasters and landslide inventory data, and require expert review before planning or safety-sensitive use. <br>
Risk: Downloaded DEM data may be recorded without proving that it was consumed by the susceptibility model. <br>
Mitigation: Verify that downloaded DEM and factor raster inputs are actually used by the run, and review the output manifest before relying on results. <br>
Risk: Susceptibility zoning is a relative likelihood output, not temporal probability or full landslide risk. <br>
Mitigation: Combine susceptibility results with trigger probability, exposure data, and domain review before using them for risk assessment. <br>
Risk: Unpinned dependencies may change runtime behavior or analysis results. <br>
Mitigation: Pin dependency versions and scan the resolved environment before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-landslide-susceptibility) <br>
- [Factor configuration](references/factor_config.json) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, CSV, GeoTIFF, GeoJSON, Shell commands, Guidance] <br>
**Output Format:** [Geospatial files, JSON manifests and metrics, CSV factor rankings, and CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes susceptibility maps, zone polygons, model metrics, factor importance, manifests, QA results, and a model card to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
