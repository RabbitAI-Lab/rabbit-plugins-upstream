## Description: <br>
Convert AutoCAD DWG files (1983-2026) to Excel databases using DwgExporter CLI. Extract layers, blocks, attributes, and geometry data without Autodesk licenses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, engineers, and CAD/BIM teams use this skill to convert DWG drawings into Excel data and analyze layers, blocks, attributes, geometry, text, and quantity-takeoff inputs without requiring Autodesk licenses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a local DwgExporter.exe binary and executes it against user-selected DWG files. <br>
Mitigation: Install and run only trusted copies of DwgExporter.exe, keep it in a controlled path, and limit execution to DWG files and output folders you choose. <br>
Risk: Untrusted or malformed CAD files may expose users to risks in the local converter workflow. <br>
Mitigation: Avoid processing untrusted DWG files; scan or sandbox files before conversion and review generated Excel/PDF outputs before relying on them. <br>


## Reference(s): <br>
- [cad2data Pipeline](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto) <br>
- [DWG to Excel Pipeline video tutorial](https://www.youtube.com/watch?v=jVU7vlMNTO0) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Files] <br>
**Output Format:** [Markdown with command examples and Python code snippets; conversions produce .xlsx files and optional .pdf files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local DwgExporter.exe and filesystem access to selected DWG files and output folders.] <br>

## Skill Version(s): <br>
2.0.0 (source: claw.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
