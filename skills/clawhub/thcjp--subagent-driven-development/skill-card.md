## Description: <br>
Coordinates multi-step implementation plans by dispatching fresh subagents per task and requiring spec-compliance and code-quality reviews before moving on. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to execute an existing implementation plan in the current session, coordinating implementation, testing, review loops, and completion checks across independent tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can lead an agent to make code edits, run commands, tests, reviews, and commits across a repository. <br>
Mitigation: Use it only for intended implementation-plan execution, review the plan first, keep branch or worktree guardrails in place, and inspect changes before merge. <br>
Risk: Poorly scoped task context or skipped review loops can produce implementation work that does not match the plan. <br>
Mitigation: Provide full task text and relevant context to each subagent, require spec-compliance review before code-quality review, and repeat review loops until issues are resolved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/subagent-driven-development) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands] <br>
**Output Format:** [Markdown instructions with workflow steps, examples, and inline command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May result in repository edits, tests, reviews, and commits when used by an agent with the necessary tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
