## Description: <br>
Maps construction data to standard ontologies and creates semantic mappings between different data schemas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, construction data teams, and project-management assistants use this skill to map user-provided CSV, Excel, JSON, or direct construction data into construction ontologies such as IFC, COBie, Uniclass, OmniClass, MasterFormat, and related schemas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Filesystem access for project data and exports can expose unintended files or write outputs to the wrong destination if paths are too broad. <br>
Mitigation: Provide specific input files, review export destinations, and confirm CSV, Excel, or JSON outputs before writing them. <br>
Risk: Ontology matches may be incomplete or low confidence for custom or ambiguous construction data. <br>
Mitigation: Review mapping confidence, unmapped fields, and recommendations before using the results in downstream reporting or data exchange. <br>


## Reference(s): <br>
- [DataDrivenConstruction homepage](https://datadrivenconstruction.io) <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/ontology-mapper) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown reports with structured tables, Python examples, and optional CSV, Excel, or JSON export guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes user-provided project data or file paths; requires Python 3 when running the documented mapper code.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata; artifact claw.json declares 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
