## Description: <br>
Twenty CRM lets an agent read, create, update, and delete CRM data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect, retrieve, create, update, and delete Twenty CRM records through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete Twenty CRM records through OOMOL-brokered access. <br>
Mitigation: Review write and delete payloads carefully and require explicit user approval before running state-changing actions. <br>
Risk: The skill depends on trusting OOMOL to broker the connected Twenty CRM account. <br>
Mitigation: Install only when OOMOL is an approved broker for the workspace and agent-managed CRM access is intended. <br>


## Reference(s): <br>
- [Twenty CRM homepage](https://twenty.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twenty-crm) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands call the OOMOL oo CLI and may return JSON responses from Twenty CRM actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
