## Description: <br>
Generates disaster recovery plans for services or systems, including RPO/RTO targets, failure scenario runbooks, backup and restore procedures, DR testing cadence, and communication templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and on-call responders use this skill to draft operational disaster recovery documentation for a service or system. It helps define measurable recovery targets, scenario-specific runbooks, backup validation, testing cadence, and incident communications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated runbook commands may be powerful or unsafe if used without adapting them to the actual service and environment. <br>
Mitigation: Have responsible engineering, SRE, and security teams review commands, replace placeholders carefully, and test procedures in safe environments before relying on them during an incident. <br>
Risk: Incorrect RPO/RTO values, contacts, or backup assumptions could make the disaster recovery plan misleading during an outage. <br>
Mitigation: Validate recovery targets, escalation contacts, backup locations, and restore procedures with service owners and business stakeholders before publishing the plan. <br>
Risk: Security breach recovery steps can interfere with containment or forensic preservation if responders self-remediate too early. <br>
Mitigation: Require security team involvement for breach or ransomware scenarios before restoring from backup or resuming normal operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/disaster-recovery-plan) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/disaster-recovery-plan.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with tables, checklists, templates, and inline shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes placeholders that must be replaced with service-specific infrastructure, contacts, thresholds, and commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
