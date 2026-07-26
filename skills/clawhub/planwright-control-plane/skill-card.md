## Description: <br>
PlanWright Control Plane helps coding agents coordinate shared objectives, claim work, record progress, and maintain an audit trail through PlanWright MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[toddamerrill](https://clawhub.ai/user/toddamerrill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill when one or more coding agents need a shared control plane for objectives, claims, progress updates, test records, and acceptance handoff. It is especially relevant for parallel agent sessions where collision avoidance and auditable evidence of agent-authored changes matter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PlanWright may record or store repository diffs, test output, project notes, and context files when agents use the audit workflow. <br>
Mitigation: Review what the PlanWright MCP server records and avoid sending sensitive private-repository content unless that storage is approved. <br>
Risk: PlanWright tool calls can fail or operate without the intended project context if the agent has not anchored to the repository first. <br>
Mitigation: Call planwright_set_repo with an explicit repository name or project ID before listing, claiming, or updating objectives. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/toddamerrill/skills/planwright-control-plane) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with ordered workflow steps, MCP tool names, and operational notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PlanWright MCP tools; ClawHub metadata indicates PLANWRIGHT_TOKEN is the primary environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
