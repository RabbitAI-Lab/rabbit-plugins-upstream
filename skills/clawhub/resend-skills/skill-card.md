## Description: <br>
Helps agents work with the Resend email API for sending, receiving, templates, webhooks, domains, contacts, broadcasts, automations, logs, API keys, and SDK setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[christina-de-martinez](https://clawhub.ai/user/christina-de-martinez) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-assisted engineering workflows use this skill to implement and troubleshoot Resend email integrations, including transactional email, inbound webhooks, account resources, and SDK setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent using this skill may send live email, enable automations, or update/delete contacts in a Resend account. <br>
Mitigation: Require explicit confirmation before sending email, enabling automations, or deleting/updating contacts. <br>
Risk: Resend API keys, webhook signing secrets, logs, and email bodies can expose sensitive account or message data. <br>
Mitigation: Use scoped Resend API keys, keep secrets in environment variables or a secret manager, and avoid printing raw log bodies or webhook signing secrets. <br>
Risk: Unverified webhook requests or inbound email content can trigger actions from untrusted input. <br>
Mitigation: Verify webhook signatures, use raw request bodies for verification, and apply additional safeguards before acting on inbound email content. <br>
Risk: Retries or batch sends can create duplicate or unintended email delivery. <br>
Mitigation: Use idempotency keys, validate batch payloads before sending, and follow Resend retry and error-handling guidance. <br>


## Reference(s): <br>
- [Resend Skill Documentation](https://resend.com/docs/resend-skill) <br>
- [Resend Skills Repository](https://github.com/resend/resend-skills) <br>
- [Resend Agent Skills](https://resend.com/agent-skills) <br>
- [ClawHub Skill Page](https://clawhub.ai/christina-de-martinez/skills/resend-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Resend SDK examples, REST API examples, environment variable requirements, and operational gotchas.] <br>

## Skill Version(s): <br>
3.3.3 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
