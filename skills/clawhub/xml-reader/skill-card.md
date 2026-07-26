## Description: <br>
Read and parse XML from construction systems - P6 schedules, BSDD exports, IFC-XML, COBie-XML. Convert to pandas DataFrames. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, engineers, and construction data practitioners use this skill to parse P6, BSDD, IFC-XML, and COBie-XML files into structured pandas DataFrames for review, analysis, and export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Untrusted XML files can be unexpectedly large or crafted to stress parsers. <br>
Mitigation: Use trusted inputs where possible, avoid huge XML files, and consider sandboxing or hardened XML parsing for attacker-supplied data. <br>
Risk: The skill reads local XML files selected by the user. <br>
Mitigation: Install and use it only when the agent is expected to access local construction XML data that the user chooses. <br>


## Reference(s): <br>
- [Xml Reader on ClawHub](https://clawhub.ai/datadrivenconstruction/skills/xml-reader) <br>
- [Data Driven Construction](https://datadrivenconstruction.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with structured tables, summaries, and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May offer Excel, CSV, or JSON export options for parsed construction XML data.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
