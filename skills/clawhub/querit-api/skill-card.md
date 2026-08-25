## Description:

Helps developers build and debug Querit.ai integrations for live web search and page-content extraction with /v1/search and /v1/contents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vinkybb](https://clawhub.ai/user/vinkybb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, smoke-test, and troubleshoot Querit.ai API integrations in applications, RAG pipelines, and agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, prompts, customer data, private URLs, or regulated content may be sent to the external Querit.ai service.

Mitigation: Use the skill only for approved Querit.ai integrations and avoid sending sensitive inputs unless organizational policy permits that use.

Risk: The required QUERIT_API_KEY could be exposed through source code, logs, notebooks, or committed configuration.

Mitigation: Store the key in an environment variable or secret manager, never hardcode it, and redact authorization headers from logs.

Risk: Search snippets can contain HTML fragments and optional or missing fields, which can break naive renderers or downstream model prompts.

Mitigation: Treat result fields as optional, sanitize snippets before display or model use, and normalize response data before passing it downstream.

Risk: Page-content crawls can partially fail while still returning HTTP 200.

Mitigation: Join contents results to statuses by id, track failures separately from successes, and avoid recording failed fetches as empty documents.

Risk: Batch integrations can hit plan-dependent rate limits or endpoint entitlements.

Mitigation: Verify each endpoint with the smoke-test script, use client-side QPS limiting, and retry only rate-limit or transient server errors with backoff.

## Reference(s):

- [Querit homepage](https://www.querit.ai)
- [Querit official documentation](https://www.querit.ai/en/docs/overview/about)
- [Querit playground](https://www.querit.ai/en/playground)
- [Search API reference](references/search-api.md)
- [Contents API reference](references/contents-api.md)
- [Python integration guide](references/python-integration.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request examples, integration guidance, smoke-test commands, response-shape notes, and troubleshooting steps.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
