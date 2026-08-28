## Description:

创建、读取、修改和导出报价单、收款收据、送货单等业务单据，并通过 AI Skills 平台 API 返回结构化结果和私有 PDF。

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and agents use this skill to create, read, update, and export quotes, receipts, and delivery notes from user-provided transaction facts. It is useful when the user needs structured document data and a private PDF generated through the AI Skills platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business document details are sent to the AI Skills platform or the configured self-hosted endpoint.

Mitigation: Use the skill only when the user accepts sending invoice, receipt, delivery, customer, amount, and item details to that endpoint.

Risk: The API key can authorize paid business-document operations if exposed.

Mitigation: Store BUSINESS_DOCUMENTS_API_KEY only in environment configuration and do not reveal it in chat, logs, or artifacts.

Risk: Create, update, and export operations may deduct platform wallet balance.

Mitigation: Tell the user before paid operations and confirm the endpoint and billing headers when available.

Risk: Private PDF artifact links may expose document contents if shared beyond the current user.

Mitigation: Provide download links only to the current user and avoid publishing artifact URLs.

Risk: Retrying uncertain network requests with a new idempotency key could create duplicate documents.

Mitigation: Reuse the same idempotency key for the same business action and report reconciliation_required when the final state cannot be confirmed.

## Reference(s):

- [AI Skills Platform](https://ai-skills.open-idea.net)
- [Business Documents Product Page](https://ai-skills.open-idea.net/skills/business-documents)
- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Polling](references/HTTP-REQUESTS.md)
- [Behavior, Security, and Error Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request and response details, shell commands, structured document results, and private PDF artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and BUSINESS_DOCUMENTS_API_KEY; uses idempotency keys and may poll platform tasks for asynchronous operations.]

## Skill Version(s):

1.0.0 (source: server release metadata and packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
