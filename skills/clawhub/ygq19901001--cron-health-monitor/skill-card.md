## Description: <br>
Cron Health Monitor helps OpenClaw agents monitor cron-job health, diagnose common failure modes, and delegate repair actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ygq19901001](https://clawhub.ai/user/ygq19901001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to inspect OpenClaw cron jobs, detect silent failures, classify recurring errors, and route repair work with verification steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents toward operational cron changes, including cron updates, forced runs, schedule changes, delivery changes, provider or model changes, filesystem writes, and disabling jobs. <br>
Mitigation: Set explicit approval rules before use, require logs for each repair action, and keep a rollback path for every cron change. <br>
Risk: Automated repair delegation may apply an incorrect fix or mask a failed cron job if outputs are not verified. <br>
Mitigation: Require manual review of proposed repairs and verify each repaired job with a forced run, state check, and expected-output inspection. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ygq19901001/skills/cron-health-monitor) <br>
- [Common Errors](references/common-errors.md) <br>
- [Repair Playbook](references/repair-playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose cron updates, forced runs, schedule changes, delivery changes, provider/model changes, filesystem writes, and disabling jobs; review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
