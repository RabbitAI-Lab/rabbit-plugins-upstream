## Description: <br>
Generates vector buffers, dissolves merged buffer geometry, performs overlay analysis, and reports area statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run local vector buffer analysis against synthetic or local GeoJSON inputs and produce GIS-ready output files plus run statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports unrelated network, credential-management, and persistence helpers outside the advertised offline buffer-analysis purpose. <br>
Mitigation: Review before installing, install only in an isolated environment, and ask the publisher to remove or clearly document the extra modules. <br>
Risk: The security guidance notes hardcoded fallback credentials and code paths that read local secret files. <br>
Mitigation: Avoid granting the skill access to home-directory secrets or credential files unless those modules have been reviewed and are required for the deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-buffer-analysis) <br>
- [README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown guidance with command examples; generated runtime artifacts are GeoJSON and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI writes buffers.geojson, dissolved_buffer.geojson, buffer_stats.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
