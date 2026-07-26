## Description: <br>
Playbook-driven incident response with MITRE ATT&CK mapping, evidence collection, timeline reconstruction, containment procedures, and post-incident reporting for ARGUS environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1beekeeper](https://clawhub.ai/user/1beekeeper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security responders and operators use this skill to follow structured incident-response playbooks for triage, evidence collection, forensic analysis, containment, impact assessment, remediation, and post-incident reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live containment commands can block traffic, terminate sessions, or lock accounts on production systems. <br>
Mitigation: Use the commands only in authorized incident-response work, confirm targets manually, and prepare rollback steps before changing firewall rules or account state. <br>
Risk: Evidence collection commands may access sensitive host data and require elevated privileges. <br>
Mitigation: Review every sudo command before use, capture hashes for collected evidence, and store evidence only in approved secure locations. <br>
Risk: Generated playbooks provide operator guidance but do not enforce case-specific safety checks. <br>
Mitigation: Treat the guidance as a playbook for trained responders and require human approval before executing destructive or state-changing actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/1beekeeper/skills/incident-responder) <br>
- [Publisher profile](https://clawhub.ai/user/1beekeeper) <br>
- [ARGUS project homepage](https://github.com/nousresearch/argus) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell command blocks and incident report templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operator playbooks, command templates, evidence paths, and report scaffolding for Linux incident-response workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
