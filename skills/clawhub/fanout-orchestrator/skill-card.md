## Description: <br>
Dispatch parallel sub-tasks across specialized agents instead of serializing through one loop when a task naturally decomposes into independent streams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oonyl](https://clawhub.ai/user/oonyl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to split independent research, review, synthesis, analysis, writing, or coding work across parallel specialist sessions and combine the results into a concise synthesis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Parallel subtasks may expose sensitive context to multiple spawned sessions or OpenProse runs. <br>
Mitigation: Confirm streams are independent and limit each spawned task to the minimum context needed before dispatch. <br>
Risk: Parallel execution may increase tool, network, or compute use compared with a single-agent response. <br>
Mitigation: Use fan-out only for tasks with two or more meaningful independent streams and review the synthesized output before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oonyl/skills/fanout-orchestrator) <br>
- [Publisher profile](https://clawhub.ai/user/oonyl) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with optional inline shell commands and structured synthesis sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include per-stream results, synthesis, tradeoffs or contradictions, and practical guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
