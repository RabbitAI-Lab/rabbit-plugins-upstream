## Description: <br>
补全ArcGIS Pro深度学习训练数据缺失文件，支持9种元数据格式和4种图像格式，自动生成esri_model_definition.emd、esri_accumulated_stats.json、map.txt、stats.txt。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongjiekun](https://clawhub.ai/user/gongjiekun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
ArcGIS Pro users and geospatial ML practitioners use this skill to repair exported deep-learning training-data folders when ArcGIS Pro export reaches 100% but omits required metadata, statistics, mapping, or summary files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running the script can permanently delete existing nonstandard .json and .emd files in the selected dataset root. <br>
Mitigation: Run only on a copied or backed-up training-data directory, and prefer a dry run or explicit cleanup flag before broad use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongjiekun/skills/arcgis-training-data-fix) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python script usage and generated ArcGIS training-data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The included script writes esri_model_definition.emd, esri_accumulated_stats.json, map.txt, and stats.txt into the selected training-data directory.] <br>

## Skill Version(s): <br>
5.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
