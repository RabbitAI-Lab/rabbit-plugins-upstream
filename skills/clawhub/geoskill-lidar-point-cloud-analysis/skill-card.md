## Description: <br>
Reads LAS/LAZ/COPC point clouds to compute statistics, classification QA, DEM/DSM/CHM rasters, cross-sections, density maps, and quality reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and data engineers use this skill to run local LiDAR point cloud analysis, generate terrain and canopy products, assess classification and density quality, and produce machine-readable QA reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The analysis writes request metadata, manifests, QA reports, logs, and geospatial outputs to the selected output directory, which may expose sensitive location or dataset details. <br>
Mitigation: Use a private output directory for sensitive point clouds, restrict sharing of generated manifests and logs, and review outputs before publishing or moving them to shared storage. <br>
Risk: Dependencies are not pinned in requirements.txt, which can lead to different behavior across production or shared environments. <br>
Mitigation: Pin and review dependency versions before production use, especially for laspy, rasterio, numpy, scipy, and geoskill-data-fetcher. <br>
Risk: The artifact documents simplified ground classification, no vertical datum transformation, and no streaming implementation for large LAS inputs. <br>
Mitigation: Validate outputs against domain QA expectations, confirm CRS and vertical datum compatibility before relying on products, and test large datasets in a controlled environment. <br>


## Reference(s): <br>
- [LiDAR standards and quality metrics](references/lidar_standards.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lidar-point-cloud-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated analysis artifacts include GeoTIFF rasters, GeoJSON profiles, JSON QA reports, manifests, metadata, and logs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local LAS/LAZ point cloud inputs for real analysis; without input it can run a synthetic workflow. Outputs are written to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
