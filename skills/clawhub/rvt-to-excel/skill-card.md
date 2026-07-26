## Description: <br>
Convert RVT/RFA files to Excel databases. Extract BIM element data, properties, and quantities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, BIM engineers, and construction data teams use this skill to convert Autodesk Revit RVT/RFA files into structured Excel data for reporting, quantity takeoffs, analytics, and downstream cost-estimation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill invokes a local RvtExporter.exe and depends on that executable's behavior. <br>
Mitigation: Install or bundle the exporter only from a trusted source and review it before use. <br>
Risk: Batch exports write conversion outputs to local paths and may overwrite existing files. <br>
Mitigation: Review input and output directories before batch runs and keep backups of important project files. <br>


## Reference(s): <br>
- [cad2data Revit conversion pipeline](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, files] <br>
**Output Format:** [Markdown guidance with command examples and Python code; the local exporter produces Excel workbooks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local filesystem access and a trusted RvtExporter.exe installation; export options can add bounding boxes, room associations, schedules, and PDFs.] <br>

## Skill Version(s): <br>
2.0.0 (source: claw.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
