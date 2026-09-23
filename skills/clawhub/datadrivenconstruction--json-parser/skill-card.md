## Description:

Parse and validate JSON data from construction APIs, IoT sensors, and BIM exports. Transform nested JSON to flat DataFrames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction)

### License/Terms of Use:

MIT

## Use Case:

Developers, data engineers, and construction project teams use this skill to parse, validate, flatten, summarize, and export JSON data from construction APIs, BIM metadata, IoT sensor feeds, and related project data sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes user-provided or referenced files, so unintended file paths could expose data the user did not mean to share with the agent.

Mitigation: Provide only files intended for parsing and review file paths before execution.

Risk: The runtime instructions mention CSV and Excel handling even though the documented implementation is JSON-focused.

Mitigation: Confirm the expected input format before processing and report unsupported formats clearly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/datadrivenconstruction/skills/json-parser)
- [Publisher Profile](https://clawhub.ai/user/datadrivenconstruction)
- [Data Driven Construction Homepage](https://datadrivenconstruction.io)
- [SKILL.md](artifact/SKILL.md)
- [instructions.md](artifact/instructions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with Python examples, structured tables, summaries, and export guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can present validation results, summary statistics, key findings, and suggested CSV, Excel, or JSON export options.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
