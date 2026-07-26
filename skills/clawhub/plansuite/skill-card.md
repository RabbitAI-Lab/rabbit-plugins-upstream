## Description: <br>
PlanSuite guides agents through file-based project planning, plan finalization, and checkpointed execution with progress and findings logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[double729](https://clawhub.ai/user/double729) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use PlanSuite to create project plans with milestones, freeze approved plans, and execute work in separate sessions while maintaining progress and findings logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates or updates local planning files that may contain project scope, decisions, findings, and rollback notes. <br>
Mitigation: Review task_plan.md, progress.md, and findings.md before continuing work, and avoid placing secrets or sensitive credentials in those files. <br>
Risk: Executing from an unfinalized or mismatched plan could lead the agent to perform work outside the user's intended scope. <br>
Mitigation: Only proceed after the finalized plan matches the requested goal, constraints, and definition of done. <br>


## Reference(s): <br>
- [PlanSuite ClawHub skill page](https://clawhub.ai/double729/skills/plansuite) <br>
- [templates/task_plan.md](artifact/templates/task_plan.md) <br>
- [templates/progress.md](artifact/templates/progress.md) <br>
- [templates/findings.md](artifact/templates/findings.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Guidance] <br>
**Output Format:** [Markdown files and concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates task_plan.md, progress.md, and findings.md in the active project.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
