## Description: <br>
多代理开发 helps an agent coordinate fresh coding subagents to execute an implementation plan with task decomposition, selective parallel work, staged reviews, and context isolation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill when they already have an implementation plan and want an agent to divide relatively independent coding tasks across subagents, enforce staged specification and code-quality reviews, and keep task context isolated. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to coordinate subagents that run commands and modify code. <br>
Mitigation: Use it in a clean branch or worktree, inspect the resulting commits, and review changes before merging. <br>
Risk: Parallel subagent work can conflict when tasks touch the same files or have unclear dependencies. <br>
Mitigation: Only parallelize independent tasks, keep shared-file or dependent tasks serial, and fall back to serial execution when conflicts appear. <br>
Risk: A vague implementation plan can lead subagents to produce work that does not match the intended scope. <br>
Mitigation: Start with a clear implementation plan, provide full task context to each subagent, and require specification and code-quality reviews before moving on. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/multi-agent-dev-v2) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands] <br>
**Output Format:** [Markdown workflow guidance with code, command, review, and status summaries produced by the agent during development] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Coordinates implementation, specification review, code-quality review, and final review steps; no extra API key is required by the skill itself.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
