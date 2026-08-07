## Description: <br>
Youd简化法结合地质地下水位与PGA的液化指数评估 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and geotechnical engineers use this skill to run local earthquake liquefaction risk assessments from synthetic scenarios or multi-band GeoTIFF inputs. It produces liquefaction potential index, factor-of-safety, parameter, and run-manifest outputs for review and downstream mapping. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact includes broader reusable geospatial code that can access networks and local credential stores beyond the documented local liquefaction workflow. <br>
Mitigation: Review the package before installation and remove or audit credential helpers and hardcoded Earthdata credentials before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-earthquake-liquefaction-risk) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, GeoTIFF, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF rasters, JSON manifests, and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces liquefaction_index.tif, factor_of_safety.tif, liquefaction_params.json, and output-manifest.json when the CLI is run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
