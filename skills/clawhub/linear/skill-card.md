## Description: <br>
Query and manage Linear issues, projects, and team workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manuelhettich](https://clawhub.ai/user/manuelhettich) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and project teams use this skill to query Linear work items, summarize team status, and perform issue workflow actions from an agent-assisted shell workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create comments and issues, and can change issue status, assignment, and priority when a Linear API key is available. <br>
Mitigation: Use a least-privilege Linear API key where possible and review agent requests before allowing write actions. <br>
Risk: The Linear API key grants access to workspace data and actions available to that credential. <br>
Mitigation: Provide the key through the LINEAR_API_KEY environment variable, avoid placing it in prompts or files, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [Linear](https://linear.app) <br>
- [Linear GraphQL API endpoint](https://api.linear.app/graphql) <br>
- [ClawHub skill page](https://clawhub.ai/manuelhettich/skills/linear) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and plain-text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LINEAR_API_KEY, curl, and jq; command output reflects the connected Linear workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
