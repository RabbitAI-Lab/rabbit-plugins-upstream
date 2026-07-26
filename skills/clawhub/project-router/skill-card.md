## Description: <br>
Project Router helps agents detect a workspace, read project context, manage a local .project bundle, run standardized project targets, and expose those actions through a CLI and MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[safatinaztepe](https://clawhub.ai/user/safatinaztepe) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering agents use this skill to bootstrap project-local context, inspect task and artifact state, and run named build, test, lint, deploy, or other workspace targets from a consistent interface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project-defined targets can execute shell commands from .project/targets.json. <br>
Mitigation: Install only in trusted workspaces, inspect .project/targets.json before running targets, and review command output before relying on results. <br>
Risk: Plan application can write project files and update .project artifacts. <br>
Mitigation: Inspect generated plan JSON before applying it and use version control or backups to review and recover file changes. <br>
Risk: The MCP server delegates to a local project CLI binary. <br>
Mitigation: Enable the MCP server only for familiar repositories and verify it points to the reviewed project CLI rather than an unrelated local binary. <br>


## Reference(s): <br>
- [Project Router ClawHub listing](https://clawhub.ai/safatinaztepe/skills/project-router) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Terminal text, Markdown project context, JSON plans and receipts, and MCP text results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute project-defined shell commands and write .project plan/apply artifacts when invoked.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
