## Description: <br>
Unified planning and execution workflow that creates file-based plans with sub-plans, freezes finalized plans, and supports separate execution sessions with checkpoints and progress and findings logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[double729](https://clawhub.ai/user/double729) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and project agents use PlanSuite to create structured task plans with milestones, finalize them for controlled execution, and maintain local progress and findings logs across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes local markdown planning, progress, and findings files during use. <br>
Mitigation: Review task_plan.md, progress.md, and findings.md during use and before relying on the recorded plan or decisions. <br>
Risk: Some skill instructions and templates are in Chinese, which may reduce clarity for users who do not read Chinese. <br>
Mitigation: Use the skill with a user or reviewer who can read the instructions, or translate the generated planning files before acting on them. <br>


## Reference(s): <br>
- [PlanSuite ClawHub Skill Page](https://clawhub.ai/double729/skills/double729-plansuite) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Guidance] <br>
**Output Format:** [Markdown planning files and concise agent guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates task_plan.md, progress.md, and findings.md in the current working directory.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
