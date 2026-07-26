## Description: <br>
Twenty CRM API integration with managed authentication for managing companies, people, opportunities, notes, and tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business operators use this skill to read and manage Twenty CRM records through Maton-authenticated API examples, including contacts, deals, activities, workspace members, and connection selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify live CRM records through a Maton-authenticated Twenty connection. <br>
Mitigation: Use it only with trusted Maton access and verify the exact record ID and intended effect before any create, update, or delete operation. <br>
Risk: Multiple Twenty connections can cause requests to affect the wrong workspace. <br>
Mitigation: Specify the intended connection with the Maton-Connection header when more than one Twenty connection exists. <br>
Risk: The skill can list workspace members and manage Twenty connections in addition to CRM records. <br>
Mitigation: Limit use to users who are authorized to view workspace membership and manage the relevant Twenty connections. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/twenty) <br>
- [Maton](https://maton.ai) <br>
- [Twenty API documentation](https://docs.twenty.com/developers/extend/api) <br>
- [Twenty GitHub repository](https://github.com/twentyhq/twenty) <br>
- [Maton Community](https://discord.com/invite/dBfFAcefs2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with REST endpoints, JSON examples, and Python or JavaScript code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; write and delete examples should be executed only after confirming the target CRM record or connection.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
