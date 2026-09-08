## Description:

Business Documents helps agents create, read, update, and export quotes, receipts, and delivery notes through the AI Skills platform, returning structured document data and private PDF artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill to generate, inspect, update, and export business documents from user-provided transaction facts. Developers and agents can use it as a structured API workflow for quotes, receipts, delivery notes, and private PDF outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business document details may include customer information, amounts, and tax fields that are sent to the AI Skills platform.

Mitigation: Confirm that users are comfortable sending those details before creating, updating, reading, or exporting documents.

Risk: The required API key could be exposed in chat, logs, or generated artifacts.

Mitigation: Store the key in BUSINESS_DOCUMENTS_API_KEY and avoid displaying complete secrets in responses or logs.

Risk: Successful create, update, and export operations may charge the user's AI Skills platform balance.

Mitigation: Explain paid actions before execution and surface billing headers or safe billing summaries after requests.

Risk: A custom API base URL could route sensitive document data to an untrusted endpoint.

Mitigation: Use the default API URL unless the platform operator provides a trusted self-hosted endpoint.

## Reference(s):

- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/business-documents/API-KEY.md)
- [Operations Contract](https://ai-skills.open-idea.net/skill-docs/business-documents/OPERATIONS.md)
- [HTTP Requests and Task Polling](https://ai-skills.open-idea.net/skill-docs/business-documents/HTTP-REQUESTS.md)
- [Behavior and Error Rules](https://ai-skills.open-idea.net/skill-docs/business-documents/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with JSON request examples, shell commands, structured API responses, and private PDF artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BUSINESS_DOCUMENTS_API_KEY and curl; requests are idempotent and may return asynchronous task results.]

## Skill Version(s):

1.2.0 (source: server release metadata, packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
