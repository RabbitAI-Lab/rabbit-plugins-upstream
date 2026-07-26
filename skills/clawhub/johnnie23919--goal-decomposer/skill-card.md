## Description: <br>
Decomposes high-level natural-language goals into executable, multi-level task trees with priorities, execution order, and optional spawn hints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johnnie23919](https://clawhub.ai/user/johnnie23919) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, project managers, product managers, and operations users can use this skill to turn ambiguous or complex goals into structured task trees for planning, delegation, and execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated task trees can contain incomplete, overlapping, or misleading decomposition when the input goal is vague. <br>
Mitigation: Have a human reviewer confirm scope, dependencies, and execution order before using the plan to drive downstream work. <br>
Risk: Privileged ClawHub or maintainer workflows can affect registry assets or accounts if used against the wrong target. <br>
Mitigation: Confirm command targets, avoid broad confirmation or full-access flags, and use least-privilege accounts or tokens. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/johnnie23919/goal-decomposer) <br>
- [Publisher profile](https://clawhub.ai/user/johnnie23919) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [JSON task tree with Markdown examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes task IDs, priorities, child tasks, execution order, dependencies, and optional spawn hints; documented maximum depth is 3 levels.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
