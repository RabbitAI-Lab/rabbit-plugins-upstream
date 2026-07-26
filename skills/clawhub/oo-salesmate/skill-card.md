## Description: <br>
Salesmate (salesmate.io) enables an agent to read, create, update, and delete Salesmate CRM data through the OOMOL Salesmate connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate Salesmate CRM through an OOMOL-connected account, including listing modules and active users, fetching companies, and creating or deleting supported CRM records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Salesmate trigger wording may cause an agent to access CRM data when a request only vaguely mentions Salesmate. <br>
Mitigation: Install only when the agent is intended to access Salesmate, and avoid invoking the skill for vague mentions unless CRM data access is intended. <br>
Risk: Write and destructive actions can create CRM records or delete Salesmate products. <br>
Mitigation: Use least-privilege API credentials where possible, review proposed payloads, and require explicit approval for create, update, or delete actions before execution. <br>


## Reference(s): <br>
- [Salesmate Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-salesmate) <br>
- [Salesmate Homepage](https://www.salesmate.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
