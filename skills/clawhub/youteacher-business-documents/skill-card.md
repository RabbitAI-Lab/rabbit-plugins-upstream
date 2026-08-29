## Description:

Business Documents helps agents create, read, update, and export quotes, receipts, and delivery notes through the AI Skills platform, returning structured results and private PDF artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to turn provided transaction facts into business documents, read or update existing documents, and export private PDFs through the AI Skills platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business document contents are sent to the AI Skills platform or a configured self-hosted endpoint.

Mitigation: Confirm the endpoint before use and avoid including unnecessary sensitive fields in document requests.

Risk: The BUSINESS_DOCUMENTS_API_KEY authorizes access to the platform account.

Mitigation: Store the key only in the configured environment variable and do not expose it in chat, logs, artifacts, or examples.

Risk: Successful create, update, and export operations can spend platform wallet balance.

Mitigation: Tell the user before paid operations and check billing response headers for charged amount, currency, and remaining balance.

Risk: Retrying after an uncertain network result can create duplicate or conflicting business actions.

Mitigation: Reuse the same Idempotency-Key for the same operation and body, and report reconciliation_required when final status cannot be confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/youteacher-business-documents)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [Business Documents product page](https://ai-skills.open-idea.net/skills/business-documents)
- [API Key](references/API-KEY.md)
- [Operations](references/OPERATIONS.md)
- [HTTP Requests](references/HTTP-REQUESTS.md)
- [Behavior Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with shell command examples and JSON API request handling; runtime results include structured document data and private PDF artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BUSINESS_DOCUMENTS_API_KEY and curl; paid create, update, and export operations can spend AI Skills platform wallet balance.]

## Skill Version(s):

1.0.1 (source: server evidence metadata.packageVersion and release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
