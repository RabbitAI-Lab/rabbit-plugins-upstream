## Description: <br>
Use when building email features, emails going to spam, high bounce rates, setting up SPF/DKIM/DMARC authentication, implementing email capture, ensuring compliance (CAN-SPAM, GDPR, CASL), handling webhooks, retry logic, or deciding transactional vs marketing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[christina-de-martinez](https://clawhub.ai/user/christina-de-martinez) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product engineers use this skill to plan, implement, and troubleshoot transactional and marketing email flows, including deliverability, consent, compliance, reliability, webhook handling, and list hygiene. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email addresses, webhook payloads, API keys, webhook secrets, IP/location details, and engagement events may expose sensitive operational or user data. <br>
Mitigation: Minimize stored data, restrict access, and define retention and deletion windows before applying the examples in production. <br>
Risk: Webhook handling can be spoofed or replayed if events are accepted without verification and idempotent processing. <br>
Mitigation: Verify webhook signatures, process duplicate events idempotently, and monitor webhook failures. <br>
Risk: Retrying uncertain email sends without stable idempotency can send duplicate transactional messages. <br>
Mitigation: Use stable idempotency keys for retries and bound retry behavior with backoff. <br>
Risk: Email compliance guidance may not fully cover a specific jurisdiction or business context. <br>
Mitigation: Treat the compliance references as implementation guidance and confirm legal requirements for the specific sending program. <br>


## Reference(s): <br>
- [Email Best Practices Skill Documentation](https://resend.com/docs/email-best-practices-skill) <br>
- [Email Best Practices Repository](https://github.com/resend/email-best-practices) <br>
- [Resend Agent Skills](https://resend.com/agent-skills) <br>
- [Email Deliverability](references/deliverability.md) <br>
- [Transactional Email Best Practices](references/transactional-emails.md) <br>
- [Transactional Email Catalog](references/transactional-email-catalog.md) <br>
- [Email Capture Best Practices](references/email-capture.md) <br>
- [Marketing Email Best Practices](references/marketing-emails.md) <br>
- [Email Compliance](references/compliance.md) <br>
- [Email Types: Transactional vs Marketing](references/email-types.md) <br>
- [Sending Reliability](references/sending-reliability.md) <br>
- [Webhooks and Events](references/webhooks-events.md) <br>
- [List Management](references/list-management.md) <br>
- [DMARC Policy Modes](https://resend.com/blog/dmarc-policy-modes) <br>
- [Warming Up](https://resend.com/docs/knowledge-base/warming-up) <br>
- [Audience Hygiene](https://resend.com/docs/knowledge-base/audience-hygiene) <br>
- [Email Verification APIs](https://resend.com/blog/best-email-verification-apis) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline code blocks, command snippets, tables, and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only reference skill; no external tools or credential variables are required by the skill.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
