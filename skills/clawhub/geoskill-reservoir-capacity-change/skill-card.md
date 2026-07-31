## Description: <br>
Establish level-area-storage relationships from water surface extents, DEMs, and water level data to analyze reservoir capacity change and sedimentation trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and water-resource teams use this skill to run reservoir storage-curve analyses, estimate current capacity, compare periods, and generate uncertainty and QA outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reservoir-change claims and true multi-temporal data use may not line up cleanly with the implementation. <br>
Mitigation: Treat outputs as exploratory and validate results independently with calibrated DEM, bathymetry, gauge, and source data before engineering, safety, regulatory, or environmental use. <br>
Risk: The skill can automatically download remote data when invoked with an area and date range instead of local DEM inputs. <br>
Mitigation: Require explicit user consent for remote data access, review downloaded sources and cache/output locations, and run in a controlled environment. <br>
Risk: Unpinned dependencies can change processing behavior across installations. <br>
Mitigation: Pin and review dependency versions in an isolated environment before operational use. <br>


## Reference(s): <br>
- [Reservoir Curve Methods](references/reservoir_curve_methods.json) <br>
- [ClawHub release page](https://clawhub.ai/ruiduobao/skills/geoskill-reservoir-capacity-change) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance plus CSV and JSON analysis artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces area-level curves, storage curves, time series, uncertainty results, request metadata, dataset and output manifests, and QA checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
