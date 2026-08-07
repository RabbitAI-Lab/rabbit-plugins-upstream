## Description: <br>
Compute shortest paths, isochrones, OD matrices, and facility service coverage from OSM or user-provided road networks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and planners use this skill to run road-network travel-time analysis, service-area delineation, origin-destination matrices, facility coverage checks, and road-closure impact assessments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic public data downloads may be unsuitable for restricted environments. <br>
Mitigation: Review and approve use of OSM and Planetary Computer downloads before running auto-download mode. <br>
Risk: Unpinned dependencies can reduce reproducibility across deployments. <br>
Mitigation: Pin dependency versions in the installation environment when deterministic deployment is required. <br>
Risk: The output manifest records run parameters and file paths. <br>
Mitigation: Use an explicit output directory and avoid sensitive input paths when manifests may be shared. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Analysis] <br>
**Output Format:** [CLI guidance and generated GeoJSON, CSV, GeoTIFF, and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include routes.geojson, service_areas.geojson, od_matrix.csv, critical_edges.geojson, unserved_population.tif, and output-manifest.json.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
