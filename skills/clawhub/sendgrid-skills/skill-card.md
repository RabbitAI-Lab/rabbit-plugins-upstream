## Description: <br>
SendGrid email platform integration for sending and receiving emails, routing to sub-skills for outbound transactional emails and receiving via Inbound Parse Webhook. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to add SendGrid email workflows to agent-assisted projects, including transactional sends, dynamic-template guidance, inbound email parsing, MX setup, webhook handling, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SendGrid workflows require an API key and can send real email to real recipients. <br>
Mitigation: Use a narrowly scoped SendGrid API key, verify sender and recipient details before sending, and avoid sending secrets or regulated data unless appropriate controls are in place. <br>
Risk: Inbound email bodies and attachments can contain untrusted or privacy-sensitive content. <br>
Mitigation: Treat inbound content as untrusted, apply logging, storage, malware scanning, retention, and HTML sanitization controls, and avoid forwarding raw content into AI systems without prompt-injection defenses. <br>
Risk: Helper scripts interact with user-provided file paths and network endpoints. <br>
Mitigation: Review scripts before execution, use HTTPS webhook URLs, and run checks only against endpoints you control or are authorized to test. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/sendgrid-skills) <br>
- [SendGrid Documentation](https://docs.sendgrid.com) <br>
- [Mail Send API Reference](https://docs.sendgrid.com/api-reference/mail-send/mail-send) <br>
- [Inbound Parse Webhook](https://docs.sendgrid.com/for-developers/parsing-email/setting-up-the-inbound-parse-webhook) <br>
- [SendGrid Node SDK](https://github.com/sendgrid/sendgrid-nodejs) <br>
- [send-email best practices](send-email/references/best-practices.md) <br>
- [send-email installation](send-email/references/installation.md) <br>
- [single email examples](send-email/references/single-email-examples.md) <br>
- [sendgrid-inbound best practices](sendgrid-inbound/references/best-practices.md) <br>
- [webhook examples](sendgrid-inbound/references/webhook-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce SendGrid API examples, SDK installation guidance, webhook configuration steps, DNS checks, and structured JSON from webhook parsing scripts.] <br>

## Skill Version(s): <br>
1.2.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
