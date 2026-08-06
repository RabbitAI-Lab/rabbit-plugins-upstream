## Description: <br>
Establishes level-area-storage relationships from water surface, DEM, and water level data to support reservoir capacity-change and sedimentation analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to estimate reservoir storage, generate area-level and storage curves, compare storage across periods, and review uncertainty from DEM, water-level, and water-boundary inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outputs may be mistaken for verified multi-period sedimentation or capacity-change evidence when they are based on synthetic data or a single DEM calculation. <br>
Mitigation: Treat outputs as modeling aids, require explicit DEM and water-level inputs, and review generated manifests before using results in operational decisions. <br>
Risk: Absolute storage estimates can be biased by public DEM limitations, sediment deposition, mismatched vertical datums, or non-coincident water-level and imagery dates. <br>
Mitigation: Use calibrated local data where available, document DEM and water-level datums, and prefer relative comparisons unless absolute storage has been independently validated. <br>
Risk: Bounding box, date, or AOI options may not provide reliable evidence that the requested area and time range affected the analysis run. <br>
Mitigation: Review request, dataset, output, and QA manifests for each run and avoid relying on bbox/date/AOI-only workflows until implementation behavior is verified. <br>


## Reference(s): <br>
- [Reservoir curve methods](references/reservoir_curve_methods.json) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands, Guidance] <br>
**Output Format:** [CSV and JSON files with command-line guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces curve tables, time series, manifests, QA data, and Monte Carlo uncertainty outputs.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
