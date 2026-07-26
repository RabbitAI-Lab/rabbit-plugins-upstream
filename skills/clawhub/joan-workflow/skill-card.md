## Description: <br>
Joan Workflow guides agents on Joan's workspace, pod, todo, plan, context-sync, and MCP workflows for AI-assisted development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[donny-son](https://clawhub.ai/user/donny-son) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI-assisted development teams use this skill to decide when to use Joan workspaces, pods, todos, plans, CLI commands, and MCP integration while managing project knowledge and tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Joan mutation and sync commands may change shared workspace knowledge or task state. <br>
Mitigation: Confirm the intended Joan account and workspace before using pod pushes, todo updates, plan pushes, archives, or sync commands. <br>
Risk: Generated context and MCP pod retrieval may reveal shared workspace knowledge. <br>
Mitigation: Review generated CLAUDE.md content and retrieve pods only from workspaces appropriate for the current project. <br>


## Reference(s): <br>
- [Joan Workflow on ClawHub](https://clawhub.ai/donny-son/skills/joan-workflow) <br>
- [Joan MCP server](https://joan.land/mcp/joan) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline bash and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only workflow guidance; no code execution by the skill itself.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
