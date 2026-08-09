## Description: <br>
Analyzes precision forestry imagery with canopy height modeling, crown-width allometric volume estimates, NDVI/NDRE health grading, and SAR biomass fusion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External forestry analysts, GIS practitioners, and developers use this skill to process local or synthetic remote-sensing data for forest inventory, health assessment, biomass estimation, and management recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed network, caching, download, and credential helper code beyond the advertised local forestry workflow. <br>
Mitigation: Review the helper modules before installation and remove or clearly disable them when the skill is used in sensitive environments. <br>
Risk: The security scan reports a hardcoded Earthdata password. <br>
Mitigation: Rotate and remove exposed Earthdata credentials before publication or deployment. <br>
Risk: Geospatial outputs and management recommendations can be misleading if source bands, CRS, units, or canopy thresholds are wrong for the target stand. <br>
Mitigation: Validate input band order, coordinate reference system, units, nodata handling, and threshold settings before using outputs for operational forestry decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-precision-forestry-monitoring) <br>
- [ruiduobao publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, GeoTIFF, GeoJSON, Guidance] <br>
**Output Format:** [Local raster/vector files plus JSON reports and manifests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces chm.tif, health_grade.tif, biomass_t_ha.tif, canopy_mask.tif, trees.geojson, forestry_report.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
