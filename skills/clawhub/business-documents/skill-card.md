## Description:

Creates, reads, updates, and exports quotes, receipts, and delivery notes through the AI Skills business-documents API, returning structured document data and private PDF artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill to generate, retrieve, revise, and export business transaction documents from user-provided transaction facts. It is intended for quote, receipt, and delivery-note workflows where the agent should call the AI Skills platform and return structured results plus private PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transaction details are sent to the AI Skills platform and successful create, update, or export operations may charge the user's platform wallet.

Mitigation: Tell the user before paid operations, send only document fields needed for the requested transaction, and report billing headers when returned.

Risk: The required BUSINESS_DOCUMENTS_API_KEY could be exposed in chat, logs, or generated artifacts.

Mitigation: Keep the key in the configured environment variable and never print the complete value in responses, logs, or output files.

Risk: Network uncertainty or retries could create duplicate paid documents if idempotency is not preserved.

Mitigation: Reuse the same Idempotency-Key only for the same operation and request body, and report reconciliation_required if the final state cannot be confirmed.

Risk: Business documents may contain confidential customer, pricing, or tax information.

Mitigation: Avoid unnecessary confidential fields, do not cross-reference document_id values across users, and share private artifact download links only with the current user.

## Reference(s):

- [AI Skills Platform](https://ai-skills.open-idea.net)
- [Business Documents Product Page](https://ai-skills.open-idea.net/skills/business-documents)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/business-documents/API-KEY.md)
- [Operations Contract](https://ai-skills.open-idea.net/skill-docs/business-documents/OPERATIONS.md)
- [HTTP Requests and Task Polling](https://ai-skills.open-idea.net/skill-docs/business-documents/HTTP-REQUESTS.md)
- [Behavior and Error Rules](https://ai-skills.open-idea.net/skill-docs/business-documents/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with JSON request and response summaries, shell command examples, and private PDF artifact links when returned by the platform]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns structured document metadata, billing headers, task status, and business-document-pdf artifacts; document item previews may be truncated to 10 items while the PDF remains authoritative.]

## Skill Version(s):

1.2.1 (source: release evidence and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
