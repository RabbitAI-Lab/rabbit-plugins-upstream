## Description: <br>
Automate Canva tasks via Rube MCP (Composio): designs, exports, folders, brand templates, autofill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to automate Canva design workflows through Rube MCP, including listing designs, creating designs, uploading assets, exporting files, organizing folders, and autofilling brand templates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects Canva workflows to a third-party MCP server and may expose private designs, exported files, asset URLs, or download links during automation. <br>
Mitigation: Use the skill only with approved Canva content, avoid unnecessary private-design access, and treat export URLs and generated files as sensitive material that should not be logged, shared publicly, or retained unnecessarily. <br>
Risk: Canva uploads, exports, and autofill operations are asynchronous, so using results before completion can produce failed or incomplete workflows. <br>
Mitigation: Poll the relevant job status until success or failure and only use asset IDs, design IDs, or download URLs after successful completion. <br>


## Reference(s): <br>
- [Rube MCP endpoint](https://rube.app/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/sohamganatra/skills/canva-automation) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with tool names, workflow steps, parameters, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Rube MCP and an active Canva OAuth connection; several workflows use asynchronous jobs that must be polled before consuming results.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
