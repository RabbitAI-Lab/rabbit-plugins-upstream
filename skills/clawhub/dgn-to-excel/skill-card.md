## Description: <br>
Convert DGN files (v7-v8) to Excel databases. Extract elements, levels, and properties from infrastructure CAD files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and civil or infrastructure engineers use this skill to convert Bentley MicroStation DGN files into structured Excel workbooks for element, level, cell, text, geometry, and reporting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on a separate DgnExporter.exe executable that must be trusted before use. <br>
Mitigation: Install and run the converter only from a trusted source, and confirm the exact executable path before invoking it. <br>
Risk: Recursive batch examples may process many DGN files and create same-named .xlsx outputs beside the inputs. <br>
Mitigation: Use explicit input folders and review batch scope before running recursive conversion commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/dgn-to-excel) <br>
- [datadrivenconstruction publisher profile](https://clawhub.ai/user/datadrivenconstruction) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with command and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides an agent to produce Excel conversion workflows and analysis steps; generated .xlsx files are produced by the external DgnExporter.exe tool.] <br>

## Skill Version(s): <br>
2.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
