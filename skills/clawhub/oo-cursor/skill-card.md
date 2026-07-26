## Description: <br>
This skill lets agents query connected Cursor team usage, spend, audit logs, and member data through OOMOL's Cursor connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and team administrators use this skill to retrieve Cursor team usage metrics, billing-cycle spend, audit log events, and visible team members from a connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording could route general Cursor requests into a connector that accesses private team usage, spend, audit logs, and member data. <br>
Mitigation: Use this skill only for explicit requests about connected Cursor team data; answer general Cursor product questions without invoking private account access. <br>
Risk: Cursor team usage, spend, audit logs, and member lists can expose sensitive operational or billing information. <br>
Mitigation: Review the requested action and filters before execution and retrieve only the data needed for the user's stated task. <br>


## Reference(s): <br>
- [Cursor homepage](https://cursor.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Cursor team data queries through the oo CLI; credentials are handled by OOMOL server-side.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
