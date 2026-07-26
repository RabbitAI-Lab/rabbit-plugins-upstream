## Description: <br>
Multi Agent Dev guides an agent to execute a clear implementation plan by decomposing tasks, coordinating fresh subagents, choosing serial or parallel execution, and applying staged reviews. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to carry out planned multi-task code changes with task decomposition, subagent coordination, review loops, and completion workflow guidance. It is best suited to clear implementation plans where tasks can be classified by dependency and file overlap. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can coordinate file reads and development command execution, so broad or vague requests may lead to unintended code changes. <br>
Mitigation: Use it on a branch or worktree with a clear implementation plan, and review planned tasks before execution. <br>
Risk: Parallel subagent work can conflict when tasks touch the same files. <br>
Mitigation: Parallelize only independent tasks, serialize shared-file work, and fall back to serial execution when conflicts appear. <br>
Risk: Generated code or reviews may miss integration or quality issues. <br>
Mitigation: Keep the staged review flow and run relevant tests before merging or releasing changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/multi-agent-dev) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with task plans, review findings, command examples, and implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May coordinate file reads and development commands through the hosting agent platform.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
