## Description: <br>
震后损害快速评估 - 利用震前震后 SAR/光学变化和建筑道路暴露，快速筛查疑似建筑损毁、道路阻断和受影响人口，并生成损毁概率分级与人工复核任务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External analysts, developers, and disaster-response teams can use this skill to run rapid earthquake damage screening from SAR/optical change signals, building exposure, and road exposure. Its outputs support triage and human review, not official engineering safety determinations, damage claims, or resource-allocation decisions without independent validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the skill can generate normal-looking earthquake damage outputs from synthetic data even when real input or downloaded data is requested. <br>
Mitigation: Treat synthetic or auto-downloaded outputs as demonstration or controlled-test artifacts unless the data path is confirmed to fail closed and the output provenance is reviewed. <br>
Risk: Earthquake damage estimates can affect emergency response, safety decisions, official claims, or resource allocation. <br>
Mitigation: Require independent validation and qualified human review before using outputs for operational, administrative, engineering, or compensation decisions. <br>
Risk: Remote-sensing limits such as SAR geometry requirements, cloud/shadow effects, image resolution, and scarce local ground truth can reduce building-level accuracy. <br>
Mitigation: Review QA outputs, validate against local observations or authoritative datasets, and calibrate models for local building types before relying on results. <br>


## Reference(s): <br>
- [Damage model parameters](references/damage_models.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-earthquake-damage-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Code, Shell commands, Configuration] <br>
**Output Format:** [Output directory containing NumPy arrays, GeoJSON, CSV, JSON manifests, review-task files, and run logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces damage_probability.npy, suspected_buildings.geojson, road_disruptions.geojson, impact_summary.csv, request.json, dataset-manifest.json, output-manifest.json, qa.json, and review_tiles/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
