## Description: <br>
Automate map layout with title, legend, scale bar and north arrow to PDF or PNG. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS practitioners use this skill to turn local raster map data or offline synthetic data into finished cartographic layouts with standard map elements and exportable deliverables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper modules include network, download, credential discovery, and home-directory persistence behavior beyond the advertised offline map layout workflow. <br>
Mitigation: Install only in an isolated environment, review or remove unused helper modules before deployment, and avoid running the skill where sensitive credential files are present. <br>
Risk: Local map inputs and generated outputs may contain sensitive location information. <br>
Mitigation: Use local processing controls, restrict output directories, and review generated PNG, PDF, GeoTIFF, metadata, and manifest files before sharing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-map-layout-automation) <br>
- [README](README.md) <br>
- [Skill Definition](SKILL.md) <br>
- [License](LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, configuration, markdown, guidance] <br>
**Output Format:** [Markdown with inline shell commands and generated local files such as PNG, PDF, GeoTIFF, JSON metadata, and run manifests.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill runs locally by default and can generate offline synthetic data when no local input file is provided.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
