## Description:

Build and debug Querit.ai search API integrations for POST /v1/search live web results and POST /v1/contents clean page text in applications, RAG pipelines, and agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vinkybb](https://clawhub.ai/user/vinkybb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, test, and debug Querit.ai search and page-content API integrations in applications, RAG pipelines, and agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, URLs, and optional page text are sent to Querit.ai.

Mitigation: Use the skill only when Querit.ai is the intended provider, and avoid sending sensitive or regulated data unless that use is approved.

Risk: The Querit API key can be exposed if it is logged, hardcoded, or committed.

Mitigation: Store QUERIT_API_KEY in environment or secret-manager storage, and redact Authorization headers from logs.

Risk: Rate limits, endpoint entitlements, or partial crawls can make integrations appear broken or silently reduce retrieval quality.

Mitigation: Run the provided smoke test first, throttle requests according to the account plan, and treat non-success crawl statuses as fetch failures rather than blank documents.

## Reference(s):

- [Querit API ClawHub listing](https://clawhub.ai/vinkybb/skills/querit-api)
- [Querit homepage](https://www.querit.ai)
- [Official Querit documentation](https://www.querit.ai/en/docs/overview/about)
- [POST /v1/search reference](references/search-api.md)
- [POST /v1/contents reference](references/contents-api.md)
- [Troubleshooting](references/troubleshooting.md)
- [Python integration](references/python-integration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request examples, integration code, smoke-test commands, and troubleshooting steps.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
