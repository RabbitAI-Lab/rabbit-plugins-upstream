## Description: <br>
Provides incident.io incident, action, status, and severity lookup through OOMOL's incident_io connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Incident responders and operations teams use this skill to let an agent read incident.io incidents, actions, statuses, and severities from a connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: incident.io data may contain sensitive operational or business information. <br>
Mitigation: Install only when the connected incident.io account is correct and treat returned incident data as sensitive. <br>
Risk: Requests are routed through OOMOL's oo connector. <br>
Mitigation: Use the skill only if that routing model is acceptable for the organization. <br>
Risk: Future versions may add write or destructive actions that change incident.io state. <br>
Mitigation: Review the version's listed actions and do not approve write or destructive payloads unless intentionally requested. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-incident-io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [incident.io](https://incident.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-oriented connector actions; command responses include data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
