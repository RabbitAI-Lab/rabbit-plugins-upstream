## Description: <br>
Linear同步(免费版) lets an agent use the Linear CLI to list and view issues, list teams and projects, and create basic Linear issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and project contributors use this skill to inspect Linear work queues, view issue details, check team and project state, and create simple issues from an agent-assisted command-line workflow. It is not intended for personnel performance evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Linear credentials may expose workspace data or allow issue creation beyond the user's intended scope. <br>
Mitigation: Use the least-privileged Linear API key that supports the intended task and verify the active workspace and team before running commands. <br>
Risk: Agent-driven commands can create remote Linear tasks. <br>
Mitigation: Require explicit user intent before creating issues or changing Linear configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/linear-sync-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with Linear CLI command examples and JSON-style response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an installed and authenticated Linear CLI; commands may read workspace data or create remote Linear issues.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
