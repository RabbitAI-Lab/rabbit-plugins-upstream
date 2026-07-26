## Description: <br>
Automate Bitbucket repositories, pull requests, branches, issues, and workspace management via Rube MCP (Composio). Always search tools first for current schemas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use this skill to operate Bitbucket workspaces through Rube MCP, including repository management, pull request workflows, branch operations, issue tracking, and workspace administration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connected Bitbucket permissions can allow real changes across repositories, issues, pull requests, branches, and workspaces. <br>
Mitigation: Install only with trusted Rube/Composio access, review the Bitbucket OAuth scope, and use the least-privileged account or workspace access that fits the task. <br>
Risk: Some supported operations are destructive or externally visible, including repository deletion, issue deletion, and posting comments. <br>
Mitigation: Require explicit user confirmation before deletions or comments, and verify the target workspace, repository, issue, or pull request before execution. <br>


## Reference(s): <br>
- [Rube MCP endpoint](https://rube.app/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/sohamganatra/skills/bitbucket-automation) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Tool calls, Markdown, Configuration instructions] <br>
**Output Format:** [Markdown guidance with MCP tool names, workflow sequences, key parameters, and operational cautions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Rube MCP and an active Bitbucket connection; agents should search current tool schemas before running Bitbucket operations.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
