## Description: <br>
Loop Engineering guides an agent through explicit planning, execution, observation, evaluation, repair, stopping, and experience-distillation loops for complex multi-step tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jainwong](https://clawhub.ai/user/jainwong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent builders use this skill to manage complex tasks that need iterative planning, tool execution, external verification, bounded repair, and clear stopping criteria. It is intended for work such as code generation and debugging, design implementation, content creation, data analysis, and multi-tool orchestration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can add process overhead on broad multi-step tasks. <br>
Mitigation: Use it for complex tasks that benefit from external verification and bounded repair, while leaving simple one-off questions outside the loop. <br>
Risk: Local experience notes may retain task details. <br>
Mitigation: Avoid using local retention on sensitive projects unless that retention is acceptable, or clear retained notes after the task. <br>
Risk: Iterative repair and multi-agent coordination can extend tool use. <br>
Mitigation: Respect the documented limits for iterations, tool calls, and stopping conditions before continuing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jainwong/skills/loop-engineering) <br>
- [Publisher profile](https://clawhub.ai/user/jainwong) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Structured Markdown guidance with YAML examples, checklists, and command-oriented execution summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include loop state cards, observation and evaluation objects, repair plans, multi-agent message structures, execution summaries, and local experience-bank notes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
