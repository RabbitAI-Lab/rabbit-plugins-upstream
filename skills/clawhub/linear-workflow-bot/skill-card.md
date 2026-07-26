## Description: <br>
Automates a Linear issue workflow that routes new tasks through webhook platforms, notifications, execution, Linear status updates, and optional Git synchronization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Independent developers, small teams, and agent operators use this skill to connect Linear tasks to notifications, execution steps, Linear comments and status changes, quota-aware webhook routing, and optional Git archival. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthenticated webhooks can trigger local scripts, Linear updates, and Git changes. <br>
Mitigation: Require webhook authentication or signed requests, validate event fields, and run the worker with least privilege before enabling automation. <br>
Risk: Automatic Git synchronization can push unwanted or conflicting changes. <br>
Mitigation: Keep autoPush disabled until tested, use a dedicated repository or branch, and require review for conflict handling and generated commits. <br>
Risk: API tokens for Linear, Discord, and automation platforms can be exposed or overprivileged. <br>
Mitigation: Store tokens outside the repository with restrictive permissions and grant only the minimum API scopes required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/linear-workflow-bot) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, code snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead an agent to make API calls, run local scripts, process webhooks, update Linear, send notifications, and create Git commits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
