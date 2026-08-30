## Description:

Creates, reads, updates, and exports quotes, receipts, and delivery notes through the AI Skills platform API, returning structured results and private PDFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill to turn provided transaction facts into structured business documents and private PDF artifacts. Developers and agents use it to call the AI Skills platform operations for document creation, reading, updating, and export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business document details such as customer names, contact details, tax IDs, prices, payment details, or delivery information are sent to the AI Skills platform.

Mitigation: Use the skill only when the user agrees to send those details, and do not expose API keys or private PDF links in chat, logs, artifacts, or public messages.

Risk: Paid document create, update, and export operations can consume platform wallet balance.

Mitigation: Confirm paid operations before use and rely on the product page or billing response headers for current charges and remaining balance.

Risk: Uncertain network results during document creation can cause duplicate business documents if retried with a new request identity.

Mitigation: Reuse the same Idempotency-Key for an identical retry and report reconciliation_required if the final operation status cannot be confirmed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/business-documents)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/business-documents/API-KEY.md)
- [Operations Contract](https://ai-skills.open-idea.net/skill-docs/business-documents/OPERATIONS.md)
- [HTTP Requests and Task Polling](https://ai-skills.open-idea.net/skill-docs/business-documents/HTTP-REQUESTS.md)
- [Behavior and Error Rules](https://ai-skills.open-idea.net/skill-docs/business-documents/BEHAVIOR-RULES.md)
- [Local API Key Reference](references/API-KEY.md)
- [Local Operations Reference](references/OPERATIONS.md)
- [Local HTTP Requests Reference](references/HTTP-REQUESTS.md)
- [Local Behavior Rules Reference](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [API Calls, Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON request and response details, curl commands, structured document data, and private PDF artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BUSINESS_DOCUMENTS_API_KEY and curl; create, update, and export operations may charge the user's AI Skills platform balance.]

## Skill Version(s):

1.1.1 (source: server release metadata and skill metadata.packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
