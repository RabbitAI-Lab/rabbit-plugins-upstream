## Description: <br>
Use when you have a written implementation plan to execute in a separate session with review checkpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenleiyanquan](https://clawhub.ai/user/chenleiyanquan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering agents use this skill to execute a written implementation plan in small batches, report verification results, and pause for feedback or clarification at checkpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An untrusted or unclear implementation plan could lead the agent to make incorrect changes. <br>
Mitigation: Use the skill with plans you trust, require checkpoint review before further work, and stop for clarification when instructions are unclear or verification fails. <br>
Risk: Final completion behavior may depend on the referenced finishing-a-development-branch skill. <br>
Mitigation: Review that referenced finishing skill separately before relying on the final development-branch workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chenleiyanquan/skills/executing-plans) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands] <br>
**Output Format:** [Markdown status reports with implementation artifacts and verification output as required by the plan] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes batch checkpoint reports; final completion behavior may depend on the referenced finishing-a-development-branch skill.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
