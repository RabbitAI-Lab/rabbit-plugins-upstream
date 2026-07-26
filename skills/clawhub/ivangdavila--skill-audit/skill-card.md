## Description: <br>
Audits agent skills for prompt injection, hidden instructions, data exfiltration, and supply-chain risk before install and after updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent users, and security reviewers use this skill to vet agent skill folders before install, assess updates, sweep installed skills, and respond when a skill may explain unexpected agent behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad sweeps across configured project and home skill directories and can write audit logs or quarantine data under ~/Clawic/data/skill-audit/. <br>
Mitigation: Review sweep_scope, log_verdicts, and local patterns.md settings before use so scans and audit records stay within the intended scope. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/skill-audit) <br>
- [Skill Homepage](https://clawic.com/skills/skill-audit) <br>
- [Checks](checks.md) <br>
- [Injection Patterns](injection-patterns.md) <br>
- [Hidden Content](hidden-content.md) <br>
- [Exfiltration](exfiltration.md) <br>
- [Scripts](scripts.md) <br>
- [Supply Chain](supply-chain.md) <br>
- [Update Audit](update-audit.md) <br>
- [Sweep](sweep.md) <br>
- [Incident](incident.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown audit guidance, verdicts, checklists, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write audit logs and quarantine guidance under ~/Clawic/data/skill-audit/ when configured by the user.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
