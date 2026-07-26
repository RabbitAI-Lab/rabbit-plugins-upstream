## Description: <br>
Manage n8n workflows and automations via API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pntrivedy](https://clawhub.ai/user/pntrivedy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation operators use this skill to inspect, activate, deactivate, execute, and troubleshoot n8n workflows and executions through the n8n REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect live n8n automations through workflow activation, deactivation, execution, update, and delete operations. <br>
Mitigation: Review workflow IDs, payload data, and intended effects before running generated commands or Python API methods against a real n8n instance. <br>
Risk: An n8n API key grants access to the configured n8n instance. <br>
Mitigation: Use a least-privileged API key where possible and avoid storing the key in shared shell profiles. <br>
Risk: Dependency installation may use a broad requests version range. <br>
Mitigation: Prefer installing with a constrained recent requests version. <br>


## Reference(s): <br>
- [n8n API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, Python examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose n8n API calls that affect live workflows and executions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
