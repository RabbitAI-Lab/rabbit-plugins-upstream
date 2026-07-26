## Description: <br>
Centralized permission layer for file writes, bash command execution, and MCP tool actions using configurable allow, deny, and prompt rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to centralize permission decisions for file writes, shell commands, and MCP tools. It helps route routine actions, risky operations, and denied actions through configurable policy rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security summary says enforcement paths can fail open, allowing command execution when rules, checker output, or checker files are missing. <br>
Mitigation: Use only in a sandbox or revise the policy model to deny by default and tightly limit privileged commands such as sudo. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/woai36d/skills/permission-enforcer) <br>
- [Publisher Profile](https://clawhub.ai/user/woai36d) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JavaScript and shell snippets; permission checks return JSON objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Policy-driven decisions cover file_write, bash, and mcp actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
