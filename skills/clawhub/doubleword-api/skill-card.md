## Description: <br>
Create, submit, monitor, and retrieve asynchronous batch AI inference jobs via the Doubleword API using JSONL files for large or cost-sensitive workloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pjb157](https://clawhub.ai/user/pjb157) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and teams use this skill to prepare JSONL batch requests, submit them to Doubleword's asynchronous API, monitor job status, and retrieve output or error files for large or cost-sensitive inference workloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Batch input and output files can contain prompts, generated content, or other data sent to Doubleword. <br>
Mitigation: Only upload prompts and batch files you are allowed to send to Doubleword, avoid secrets or regulated data unless your agreement permits it, and review Doubleword privacy and retention terms before use. <br>
Risk: API credentials are required to call Doubleword endpoints. <br>
Mitigation: Use a secure environment variable such as DOUBLEWORD_API_KEY and do not include API keys in batch files, committed code, or shared logs. <br>


## Reference(s): <br>
- [Doubleword Batch API Reference](references/api_reference.md) <br>
- [Doubleword API Base URL](https://api.doubleword.ai/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files] <br>
**Output Format:** [Markdown guidance with bash, JSON, JSONL, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce JSONL batch request files and command sequences for Doubleword API workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
