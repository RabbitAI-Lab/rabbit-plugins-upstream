## Description: <br>
Codex Orchestration helps Codex plan work, coordinate parallel worker agents, and manage background terminal sessions for complex tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shanelindsay](https://clawhub.ai/user/shanelindsay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Codex operators use this skill to break down larger tasks, delegate read-only or scoped implementation work to workers, and synthesize the results into a clean final response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill coordinates Codex workers that may run shell commands or operate without approval prompts. <br>
Mitigation: Use it only in trusted workspaces, keep worker prompts narrowly scoped, and prefer read-only worker assignments unless edits are explicitly intended. <br>
Risk: Parallel workers can expose sensitive project data or credentials if prompts include unnecessary context. <br>
Mitigation: Limit worker context to the minimum required files and avoid sharing private data or secrets unless necessary for the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shanelindsay/skills/codex-orchestration) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with command examples and worker prompt templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or coordinate command execution through Codex workers; review worker scopes before use.] <br>

## Skill Version(s): <br>
2.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
