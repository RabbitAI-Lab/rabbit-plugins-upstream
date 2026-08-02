## Description: <br>
WorkBuddy Tuner helps agents diagnose WorkBuddy performance issues, monitor system and context health, generate optimization plans, audit sessions, track trends, and prepare recovery or migration checklists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
WorkBuddy users and support teams use this skill to diagnose slow or unstable WorkBuddy sessions, monitor CPU, memory, disk, network, and context health, generate optimization plans, audit sessions, and plan recovery or migration before reinstalling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad local performance-monitoring and tuning authority. <br>
Mitigation: Confirm the files, sessions, processes, directories, and scan scope before running monitoring, optimization, migration, recovery, automated scan, or skill-matrix installation actions. <br>
Risk: Optimization, migration, recovery, and cleanup workflows can change local state. <br>
Mitigation: Keep dry-run mode enabled until the proposed changes are reviewed, and require explicit confirmation before applying write, delete, migration, or process-management actions. <br>
Risk: The security review flags contradictory low-risk and privacy claims. <br>
Mitigation: Avoid granting access to credentials or private session data unless the host provides clear containment and the data access need is explicit. <br>
Risk: Automated scans and tuning loops may create operational overhead or act on stale assumptions. <br>
Mitigation: Use conservative scan frequency, review generated reports before action, and validate recommendations against current system conditions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/workbuddy-tuner) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Flow Immersion SkillHub reference](https://skillhub.cn/skills/user_11064e10/flow-immersion) <br>
- [WorkBuddy Gift Claimer SkillHub reference](https://skillhub.cn/skills/user_11064e10/workbuddy-gift-claimer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and structured recommendations with inline commands or configuration steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run optimization plans, health scores, alerts, migration checklists, recovery guidance, and trend summaries.] <br>

## Skill Version(s): <br>
3.3.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
