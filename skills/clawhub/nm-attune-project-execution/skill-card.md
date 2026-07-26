## Description: <br>
Executes implementation plans with progress tracking, checkpoint validation, and quality gates after planning is complete and tasks are ready to implement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to execute existing implementation plans in dependency order, track task progress, apply TDD and checkpoint validation, and prepare completion reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may guide high-impact production migration or data-change work. <br>
Mitigation: Keep dry-run, explicit confirmation, verification, and cleanup gates in place before applying changes. <br>
Risk: Task progress or completion reports could be inaccurate if checkpoints are skipped. <br>
Mitigation: Validate acceptance criteria, tests, quality checks, and blockers at each checkpoint before marking tasks complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-execution) <br>
- [Attune plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with code, shell command, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
