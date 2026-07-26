## Description: <br>
quiet-mail helps AI agents create mailbox identities, send email, and review sent messages through a simple REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[co1onnese](https://clawhub.ai/user/co1onnese) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use quiet-mail to give AI agents an email address and outbound email capability for notifications, reports, service signups, and automation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables broad agent-controlled outbound email. <br>
Mitigation: Require explicit human approval before outbound mail, restrict allowed recipients and sending volume, and install only when an agent is intended to control an external email account. <br>
Risk: The artifact ships live-looking plaintext SMTP credentials in test scripts. <br>
Mitigation: Remove the bundled credentials, rotate any exposed mailbox passwords before use, and avoid running live SMTP test scripts. <br>
Risk: quiet-mail API keys and mailbox passwords grant access to email functions. <br>
Mitigation: Treat API keys and mailbox passwords as secrets and store them only in protected secret-management or environment-variable channels. <br>


## Reference(s): <br>
- [quiet-mail ClawHub listing](https://clawhub.ai/co1onnese/skills/quietmail) <br>
- [quiet-mail API documentation](artifact/API.md) <br>
- [quiet-mail README](artifact/README.md) <br>
- [quiet-mail webmail](https://quiet-mail.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with REST API examples, curl commands, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent setup, email-sending, sent-mail listing, deployment, and credential-handling guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
