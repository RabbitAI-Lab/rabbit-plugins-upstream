## Description:

LlMFill helps agents use the LLMFill remote service to fill Word (.docx) forms and questionnaires, manage knowledge bases for answer retrieval, and check account or API-token status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xdgaoyong](https://clawhub.ai/user/xdgaoyong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to automate AI-assisted completion of Word forms, questionnaires, and checklists, optionally grounding answers with uploaded knowledge-base documents. It also supports setup, token validation, balance checks, service discovery, and troubleshooting for LLMFill workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can send confidential, regulated, or internal Word documents and knowledge-base files to the LLMFill remote service.

Mitigation: Review data-handling requirements before installation and process only documents approved for that external service.

Risk: The skill uses long-lived API tokens for account access.

Mitigation: Protect the API token, prefer secure local permissions or environment variables, and rotate or delete exposed tokens promptly.

Risk: Changing the configured base URL can route documents and credentials through a self-hosted or proxy endpoint.

Mitigation: Use the default HTTPS LLMFill endpoint unless the alternate endpoint is intentionally trusted.

Risk: Knowledge-base deletion can remove uploaded reference data.

Mitigation: Confirm the target knowledge base before destructive deletion commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xdgaoyong/skills/llmfill)
- [LLMFill service](https://www.llmfill.com)
- [API account and configuration reference](references/api-account.md)
- [Document filling API reference](references/api-documents.md)
- [Knowledge base API reference](references/api-knowledge.md)
- [Curl usage guide](references/curl-guide.md)
- [Error reference](references/errors.md)
- [End-to-end form fill example](examples/fill-a-form.md)
- [Knowledge base setup example](examples/build-kb.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON-capable CLI output, and downloaded .docx or .zip result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote API workflows may upload user documents, poll asynchronous jobs, report estimated and actual costs, and download marked or clean results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
