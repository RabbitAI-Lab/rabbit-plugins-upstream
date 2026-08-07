## Description: <br>
Integrate terrain, geology, rainfall, land cover, roads, and historical landslide data to produce interpretable susceptibility zoning with spatial cross-validation. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run a landslide susceptibility workflow, compare logistic regression, random forest, and slope-baseline models, and generate susceptibility maps, zone polygons, validation metrics, factor importance, manifests, and QA files. Outputs should be treated as demonstration or prototype artifacts unless real factor rasters and validated landslide inventory data are supplied and reviewed by domain experts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce landslide-analysis artifacts that appear operational while relying on synthetic demo data or synthetic factor rasters. <br>
Mitigation: Use outputs only as demonstration or prototype results unless real factor-raster inputs and validated landslide inventory data are supplied, synthetic outputs are clearly labeled, and domain experts review the results. <br>
Risk: Bounding-box or AOI runs may contact Microsoft Planetary Computer to download DEM data. <br>
Mitigation: Disclose network access before execution, constrain bbox/date/cache settings, and review output-manifest.json for recorded collection, bbox, fetch timestamp, and downloaded paths. <br>
Risk: Unpinned Python dependencies can make installs and analysis outputs less reproducible. <br>
Mitigation: Pin dependency versions and record the environment before using the skill in repeatable evaluation or release workflows. <br>
Risk: Susceptibility outputs are not temporal probability, hazard, or risk assessments and are not suitable for engineering safety decisions on their own. <br>
Mitigation: Pair susceptibility outputs with trigger probability, exposure data, and qualified geotechnical review before using results for planning, safety, administrative, or compensation decisions. <br>


## Reference(s): <br>
- [factor_config.json](references/factor_config.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated geospatial, JSON, CSV, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces susceptibility.tif or susceptibility.npy, susceptibility_zones.geojson, model_metrics.json, factor_importance.csv, model_card.json, request.json, dataset-manifest.json, output-manifest.json, qa.json, and run.log.] <br>

## Skill Version(s): <br>
3.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
