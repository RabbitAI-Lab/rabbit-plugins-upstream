## Description: <br>
WorkBuddy Tuner helps diagnose WorkBuddy slowness, memory pressure, startup issues, cache buildup, session context growth, local performance trends, Windows startup items, and token usage, then proposes measured optimization steps with dry-run and backup confirmation safeguards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
WorkBuddy users and support engineers use this skill to investigate lag, high memory use, slow startup, cache growth, process issues, session history bloat, startup-item impact, and token costs before applying optimization actions. It is intended for intentional troubleshooting where the user reviews proposed cleanup, process, startup, migration, or skill-install changes before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide high-impact cleanup, process, startup, migration, or skill-install actions. <br>
Mitigation: Use it only for intentional WorkBuddy troubleshooting and require review of dry-run previews before execution. <br>
Risk: The skill may analyze local performance telemetry and session history and can retain local tuning state. <br>
Mitigation: Review local data handling before installation and avoid broad automatic activation in sensitive environments. <br>
Risk: Optimization guidance could be incorrect or misleading for a specific workstation state. <br>
Mitigation: Confirm backups and validate proposed changes against the current system before applying them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/workbuddy-tuner) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured findings, health scores, recommendations, and optional command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run plans, backup guidance, monitoring summaries, trend reports, and token-cost estimates.] <br>

## Skill Version(s): <br>
3.6.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
