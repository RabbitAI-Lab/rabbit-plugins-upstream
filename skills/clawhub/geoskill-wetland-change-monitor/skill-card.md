## Description: <br>
Monitor wetland extent, inundation frequency, and land cover transitions to identify degradation, recovery, and human encroachment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to run wetland change monitoring workflows over local raster inputs or bounded date and area requests. It supports assessment of wetland health, degradation, recovery, inundation frequency, and land cover transitions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using bbox and date-range inputs can contact Microsoft Planetary Computer and disclose the requested area and dates. <br>
Mitigation: Use local raster inputs for sensitive areas, or limit requests to approved areas and dates. <br>
Risk: Downloaded geospatial data and metadata may be stored in the output or cache directory. <br>
Mitigation: Use a controlled cache and output directory, and clear or protect generated files according to the data sensitivity. <br>
Risk: Unpinned dependencies can reduce reproducibility across deployments. <br>
Mitigation: Pin package versions in deployment environments when reproducible results are required. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Files, Analysis] <br>
**Output Format:** [CLI guidance plus GeoTIFF, GeoJSON, CSV, and JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces wetland classification, inundation frequency, vectorized change patches, transition matrices, reports, and an output manifest.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
