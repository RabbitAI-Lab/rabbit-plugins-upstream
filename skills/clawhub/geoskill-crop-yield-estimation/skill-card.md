## Description: <br>
融合遥感时序、天气、土壤和统计样本，估算地块或行政区作物产量，给出预测区间和可解释因子。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agriculture analysts can use this skill to run a crop-yield estimation workflow over CSV or GeoJSON yield labels and produce geospatial estimates, uncertainty intervals, validation metrics, and feature importance outputs. Results should be reviewed carefully before operational use because the security evidence says implemented features are synthetic prototype output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crop-yield estimates and feature importance may be mistaken for validated multisource analysis even though the security evidence says implemented features are synthetic random values. <br>
Mitigation: Use only for experimentation or code review until real, validated data ingestion replaces the synthetic feature generator and outputs are independently validated. <br>
Risk: Operational decisions could rely on prototype predictions or uncertainty intervals. <br>
Mitigation: Do not use outputs for operational crop-yield decisions; require domain review, validation against trusted labels, and documented model performance before deployment. <br>
Risk: External data download behavior and dependency pinning are not fully clarified in the security guidance. <br>
Mitigation: Review network behavior and pin dependencies before installation in controlled or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-crop-yield-estimation) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [yield_factors.json](artifact/references/yield_factors.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands and generated GeoJSON, GeoTIFF, CSV, JSON, and log files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow can produce yield_estimate.geojson, yield_estimate.tif, prediction_interval.tif, yield_by_admin.csv, feature_importance.csv, model_card.json, qa.json, request.json, dataset-manifest.json, output-manifest.json, and run.log.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter version is 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
