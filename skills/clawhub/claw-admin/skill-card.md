## Description: <br>
Provision and manage @clawemail.com Google Workspace email accounts for AI agents, including availability checks, account creation, suspension, unsuspension, and deletion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cto1](https://clawhub.ai/user/cto1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to provision and administer ClawEmail Google Workspace accounts for AI agents, including checking address availability and managing account lifecycle actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through permanent deletion of Google Workspace email accounts and associated data. <br>
Mitigation: Require manual confirmation before destructive actions and verify the target prefix before issuing delete requests. <br>
Risk: Returned passwords, OAuth connection URLs, and API keys are sensitive credentials. <br>
Mitigation: Use only API keys approved for agent use, avoid exposing credentials in logs or chat history, and store returned secrets securely. <br>


## Reference(s): <br>
- [ClawEmail service](https://clawemail.com) <br>
- [ClawEmail Admin skill page](https://clawhub.ai/cto1/skills/claw-admin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses CLAWEMAIL_API_KEY for authenticated administrative requests.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
