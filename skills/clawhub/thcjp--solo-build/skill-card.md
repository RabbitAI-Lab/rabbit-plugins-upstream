## Description: <br>
Solo Build helps an agent execute implementation plans from plan.md and spec.md by selecting tasks, using TDD or direct implementation, running checks, updating progress, and committing completed work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use Solo Build to work through existing implementation plans, resume interrupted tasks, apply TDD or direct implementation workflows, run validation checks, and keep plan progress current. It is not intended for creating plans, deployment workflows, code review, or personnel performance evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to edit project files, run local commands, execute tests, and create git commits. <br>
Mitigation: Use it only in repositories where those actions are intended, review the selected plan and task before execution, and require confirmation before commits or rollback actions in sensitive projects. <br>
Risk: The security summary flags a mismatch between broad automation authority and softer metadata or activation wording. <br>
Mitigation: Treat the skill as an active build agent rather than a passive planning aid, and scope its use to existing plan.md and spec.md workflows. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown status reports with command snippets, implementation summaries, validation results, and error details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include completed task summaries, changed-file notes, test or lint results, commit messages, and a completion signal when the required local state exists.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
