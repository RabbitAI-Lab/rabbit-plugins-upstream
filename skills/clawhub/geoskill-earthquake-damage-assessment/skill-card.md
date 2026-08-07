## Description: <br>
Rapidly screens suspected building damage, road disruptions, and affected population after earthquakes using pre- and post-event SAR/optical change signals with building and road exposure. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run earthquake damage assessment workflows, generate suspected damage outputs, and prepare manual review tasks. Outputs require independent human verification before disaster response, engineering, administrative, or compensation use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can generate earthquake damage reports from synthetic data even when real inputs or downloads are supplied. <br>
Mitigation: Treat outputs as demo/prototype results unless real input processing is fixed, label synthetic outputs clearly, and require fail-closed behavior when real imagery cannot be processed. <br>
Risk: Damage probabilities, road disruption records, and affected population estimates could be mistaken for final disaster-response or engineering determinations. <br>
Mitigation: Require independent human verification before using outputs for disaster response, safety decisions, engineering assessment, administrative determinations, or compensation workflows. <br>
Risk: Dependencies are not fully pinned, which can make installs and results less reproducible. <br>
Mitigation: Pin dependencies before serious deployment and review package permissions and data-source access paths. <br>


## Reference(s): <br>
- [Damage Models Reference](references/damage_models.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-earthquake-damage-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files] <br>
**Output Format:** [Markdown guidance plus generated NumPy, GeoJSON, CSV, JSON manifest, QA, and review-task files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include damage_probability.npy, suspected_buildings.geojson, road_disruptions.geojson, impact_summary.csv, review_tiles, request.json, dataset-manifest.json, output-manifest.json, and qa.json.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
