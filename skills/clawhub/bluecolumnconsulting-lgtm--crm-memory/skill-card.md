## Description: <br>
Gives AI agents CRM memory for sales teams using BlueColumn persistent memory, including workflows to store, recall, and search deal, contact, and pipeline context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales teams and agent developers use this skill to give an AI agent persistent CRM memory for deal, contact, owner, and pipeline context. It supports recalling current CRM state before a user interaction and storing a summary afterward. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CRM deal, owner, contact, and pipeline context may be sent to BlueColumn's external persistent memory service. <br>
Mitigation: Confirm organizational approval before installation and define what CRM data may be stored. <br>
Risk: Stored memory may include secrets, regulated personal data, or customer-sensitive information if users provide it. <br>
Mitigation: Use an approved API key, avoid secrets and regulated personal data unless explicitly authorized, and establish deletion and retention expectations. <br>


## Reference(s): <br>
- [BlueColumn API Documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub Skill Page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/crm-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and API usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends CRM memory content to an external persistent memory service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
