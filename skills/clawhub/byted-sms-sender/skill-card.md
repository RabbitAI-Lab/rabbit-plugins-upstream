## Description:

Volcengine SMS helps agents guide account setup, qualification applications, signature and template requests, single and bulk SMS sends, delivery receipts, and customer-visible analytics for China SMS workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volcengine-skills](https://clawhub.ai/user/volcengine-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, business operators, and support agents use this skill to operate a Volcengine SMS account: prepare service onboarding, create qualifications, apply for signatures and templates, send individual or bulk domestic SMS messages, and review delivery status and visible analytics.

### Deployment Geography for Use:

China domestic SMS workflows

## Known Risks and Mitigations:

Risk: The skill can operate a Volcengine SMS account, including sending SMS, launching bulk sends, creating resources, and uploading qualification documents.

Mitigation: Install only for intended Volcengine SMS account operation, review every preview carefully, and require exact confirmation before sends or batch launches.

Risk: Credentials and sensitive identity or qualification data could be exposed if collected in chat or logged.

Mitigation: Provide credentials only through browser login or local environment setup, and use the local private qualification form for sensitive documents and identity fields.

Risk: A write request may have an unknown outcome after a network or service failure.

Mitigation: Do not retry or switch paths for possible write operations; reconcile through the documented status or list actions before further action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/volcengine-skills/skills/byted-sms-sender)
- [Action public contracts](references/actions.md)
- [Application contracts](references/application-contracts.md)
- [Authentication setup](references/auth-setup.md)
- [Delivery contracts](references/delivery-contracts.md)
- [Qualification materials](references/qualification-materials.md)
- [Rules](references/rules.md)
- [Service onboarding](references/service-onboarding.md)
- [Workflows](references/workflows.md)
- [Volcengine SMS console](https://console.volcengine.com/sms)
- [Volcengine SMS send error codes](https://www.volcengine.com/docs/6361/173288?lang=zh)
- [Volcengine SMS delivery status codes](https://www.volcengine.com/docs/6361/173291?lang=zh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured command outputs, previews, status summaries, and local browser form flows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate authenticated Volcengine SMS API operations only after preview and customer authorization; sensitive qualification material is handled through local private forms.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter metadata.version is 1.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
