## Description: <br>
Provision and manage @clawemail.com Google Workspace email accounts for AI agents, including availability checks, account creation, and account lifecycle management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cto1](https://clawhub.ai/user/cto1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to create and administer @clawemail.com Google Workspace accounts for AI agents. It supports checking address availability, provisioning accounts, retrieving account status, suspending or restoring accounts, and deleting accounts when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delete Google Workspace accounts and associated data through the ClawEmail admin API. <br>
Mitigation: Require manual confirmation of the exact email prefix before delete operations, and reserve deletion for trusted operators. <br>
Risk: Admin API keys, generated passwords, and OAuth credentials can grant access to mailbox and Workspace data. <br>
Mitigation: Store CLAWEMAIL_API_KEY and returned credentials only in approved secret storage, avoid logging them, and rotate them if exposed. <br>
Risk: Suspend and unsuspend actions can affect account availability. <br>
Mitigation: Confirm the target prefix and intended lifecycle action before invoking suspend or unsuspend endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cto1/skills/clawemail-admin) <br>
- [ClawEmail service](https://clawemail.com) <br>
- [ClawEmail availability check](https://clawemail.com/check/DESIRED_PREFIX) <br>
- [Gmail sign-in](https://mail.google.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API calls, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEMAIL_API_KEY for admin endpoints; account passwords and OAuth links may be returned and must be handled as secrets.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
