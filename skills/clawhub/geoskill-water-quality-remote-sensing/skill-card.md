## Description: <br>
Estimate water quality parameters from multispectral satellite imagery using red and green bands, with optional NIR/SWIR inputs, for analysis and report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to compute water-quality indices from multispectral raster bands or documented bbox/date inputs and generate machine-readable and human-readable assessment outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented bbox/date workflow may contact external satellite data services and store downloaded data in a local cache. <br>
Mitigation: Run the skill in a controlled environment and set --cache-dir to a managed location when using satellite download inputs. <br>
Risk: Dependencies are not pinned in the artifact requirements. <br>
Mitigation: Pin or lock dependency versions before production deployment. <br>
Risk: Documentation clarity gaps can cause users to choose the wrong input mode or runtime setup. <br>
Mitigation: Review the documented prerequisites and CLI arguments before execution, especially when using bbox/date inputs or local raster files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-water-quality-remote-sensing) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated tool outputs include JSON, HTML, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes outputs to a user-selected output directory; local cache behavior may apply when using documented satellite download inputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
