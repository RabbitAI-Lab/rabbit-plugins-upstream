## Description: <br>
Set up a dedicated email address for an agent using Resend. Configure sending, receiving via webhook, inbox storage, and automated monitoring. Use when: (1) agent needs its own email identity, (2) agent needs to receive confirmation emails from external services, (3) setting up agent email for the first time, (4) agent needs to autonomously handle email verification flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[di5cip1e](https://clawhub.ai/user/di5cip1e) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to give an agent a dedicated Resend-backed email address for sending messages, receiving verification emails and notifications, storing inbound mail, and monitoring the inbox. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resend API keys and webhook secrets can be exposed through chat, logs, source control, or misconfigured environments. <br>
Mitigation: Use a dedicated Resend key and domain where possible, keep secrets in secrets management, and avoid logging or sharing secret values. <br>
Risk: Inbound email may contain sensitive account, verification, or personal information. <br>
Mitigation: Protect the mail/inbox directory, limit access to stored JSON mail files, and avoid automatic summaries of sensitive inbox contents unless the owner has approved that workflow. <br>
Risk: Unsigned or spoofed webhook requests could create untrusted inbound email records. <br>
Mitigation: Require HTTPS webhook endpoints and verify Resend webhook signatures with RESEND_WEBHOOK_SECRET before storing inbound messages. <br>


## Reference(s): <br>
- [Agent Email Setup skill](https://clawhub.ai/di5cip1e/agent-email-setup) <br>
- [directorMail.js](references/directorMail.js) <br>
- [inboundEmail.js](references/inboundEmail.js) <br>
- [Resend API](https://api.resend.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands, JSON snippets, and JavaScript code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-supplied Resend domain, API key, webhook secret, backend URL, and inbox storage path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
