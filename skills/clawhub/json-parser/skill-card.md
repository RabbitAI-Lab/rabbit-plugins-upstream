## Description: <br>
Parse and validate JSON data from construction APIs, IoT sensors, and BIM exports. Transform nested JSON to flat DataFrames. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction developers, project teams, and data analysts use this skill to parse, validate, flatten, and summarize user-provided JSON data from construction APIs, BIM exports, and IoT sensor feeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill works with files and data paths supplied by the user, so it may read sensitive project files if pointed at unrelated private directories. <br>
Mitigation: Limit use to the specific JSON, CSV, or Excel files intended for parsing and avoid directories that contain secrets or unrelated private data. <br>
Risk: The release name emphasizes JSON while the instructions also describe CSV and Excel inputs, which may surprise users about the formats handled. <br>
Mitigation: Confirm the expected input format before processing and treat CSV or Excel handling as intentional behavior only when the user requests it. <br>


## Reference(s): <br>
- [Skill homepage](https://datadrivenconstruction.io) <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/json-parser) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with structured tables, Python code examples, validation summaries, and export guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include summary statistics, key findings, error messages, and suggested fixes for user-provided data.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
