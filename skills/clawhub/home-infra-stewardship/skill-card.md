## Description: <br>
Routine NetBox, Zabbix, and homelab maintenance with responsible change authority. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators responsible for Ryan's internal homelab use this skill to perform recurring NetBox, Zabbix, and related automation maintenance while preserving escalation points for high-risk changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad recurring authority for an agent to proactively change internal infrastructure and automation with loose boundaries. <br>
Mitigation: Narrow the approved systems and define which classes of changes require confirmation before using the skill. <br>
Risk: Routine maintenance may affect NetBox, Zabbix, automation state, logs, or configuration in ways that are hard to reverse. <br>
Mitigation: Use backups, snapshots, exports, rollback paths, and verification checks before and after material service changes. <br>
Risk: Maintenance records can expose sensitive infrastructure details if written to inappropriate locations. <br>
Mitigation: Keep memory and log locations controlled, and avoid printing secrets or sensitive infrastructure details into chat or public files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/home-infra-stewardship) <br>
- [gasgangrene publisher profile](https://clawhub.ai/user/gasgangrene) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with operational steps and command recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce plans, change notes, verification summaries, and documentation updates for internal infrastructure maintenance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
