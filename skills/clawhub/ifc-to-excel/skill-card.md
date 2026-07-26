## Description: <br>
Convert IFC files (2x3, 4x1, 4x3) to Excel databases using IfcExporter CLI, extracting BIM data, properties, and geometry without proprietary software. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
BIM, construction, and data engineering teams use this skill to convert IFC model files into structured Excel data and optional 3D geometry for validation, quantity takeoff, reporting, and downstream analytics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads IFC files and writes conversion outputs in user-selected folders. <br>
Mitigation: Use trusted input and output paths, confirm target folders before batch jobs, and review generated files before sharing them. <br>
Risk: Conversion may invoke an external IfcExporter or IfcOpenShell installation. <br>
Mitigation: Use a trusted converter installation and verify the executable path before running conversion commands. <br>


## Reference(s): <br>
- [Ifc To Excel on ClawHub](https://clawhub.ai/datadrivenconstruction/skills/ifc-to-excel) <br>
- [cad2data Pipeline](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto) <br>
- [buildingSMART IFC Standard](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and Python code examples; conversion workflows may produce XLSX and DAE files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires filesystem access to read IFC inputs and write generated conversion outputs.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and claw.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
