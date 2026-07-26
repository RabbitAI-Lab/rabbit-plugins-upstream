## Description: <br>
Create and manage temporary disposable email inboxes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johanski](https://clawhub.ai/user/johanski) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to create disposable email inboxes, poll for incoming messages, retrieve message content, extract verification codes or links, extend inbox lifetime, and delete the inbox after use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Disposable inboxes may receive verification links or codes that grant access to accounts or private data. <br>
Mitigation: Use the skill only for low-risk temporary inboxes, testing, and disposable signups; avoid password resets, financial accounts, regulated data, and private correspondence. <br>
Risk: The session token controls inbox access during the temporary session. <br>
Mitigation: Treat the token like a temporary password, reuse it only for the intended inbox session, and delete the inbox when finished. <br>
Risk: Polling or creating many inboxes can conflict with service limits or target-site acceptable-use rules. <br>
Mitigation: Poll responsibly, respect the target service's rules, and avoid unnecessary inbox creation. <br>


## Reference(s): <br>
- [Shitty Email service](https://shitty.email) <br>
- [Shitty Email skill on ClawHub](https://clawhub.ai/johanski/skills/shitty-email) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and temporary X-Session-Token reuse for inbox operations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
