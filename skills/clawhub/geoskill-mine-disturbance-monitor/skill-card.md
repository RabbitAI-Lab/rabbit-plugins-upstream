## Description: <br>
Monitor surface disturbance at mining sites using multi-temporal optical/SAR/DEM data, detecting bare land, pits, dumps, roads, and vegetation removal while tracking boundary violations and area statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, geospatial analysts, mining compliance teams, and developers use this skill to analyze multi-year mine-site imagery, identify surface disturbance patterns, and produce evidence files for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make outbound requests for public satellite data and store downloaded imagery plus generated analysis files locally. <br>
Mitigation: Run it only where outbound access and local imagery storage are approved; set explicit cache and output directories so generated files can be audited and removed. <br>
Risk: Disturbance classifications and outside-boundary outputs may be unsuitable for compliance decisions if imagery, DEMs, boundaries, CRS handling, or dependency versions are wrong for the site. <br>
Mitigation: Review outputs against source imagery and authoritative permit boundaries before relying on them, and pin and scan resolved Python dependencies for production or regulated use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-mine-disturbance-monitor) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, guidance, files] <br>
**Output Format:** [CLI guidance plus local GeoJSON, GeoTIFF, CSV, and JSON manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces disturbance_by_year.geojson, outside_boundary.geojson, disturbance_type.tif when a reference raster is available, summary.csv, and output-manifest.json.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
