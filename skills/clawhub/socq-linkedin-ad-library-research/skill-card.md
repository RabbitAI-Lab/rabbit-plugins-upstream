## Description:

Research public Linkedin Ad Library content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and research agents use this skill to select SocQ LinkedIn Ad Library endpoints, estimate credit usage, submit public-data collection tasks, follow pagination, and report normalized ad library findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires SOCQ_API_KEY access for SocQ MCP, CLI, or REST requests.

Mitigation: Keep the key in the process environment, avoid prompts, URLs, committed files, and retained command history, and use API-key limits such as rate, credit, and IP controls when available.

Risk: SocQ requests may consume paid credits, especially for large-volume or multi-endpoint research.

Mitigation: Review expected costs, check account balance or limits, reduce scope when needed, and obtain confirmation before submitting large paid runs.

Risk: Asynchronous tasks, pagination limits, provider failures, or unsupported filters can produce incomplete coverage.

Mitigation: Track task IDs, poll to a terminal state, preserve pagination cursors, report failed requests and unsupported filters, and avoid claiming completeness when collection stops early.

## Reference(s):

- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ LinkedIn Ad Library API documentation](https://docs.socq.ai/api-manual/linkedin-ad-library)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Linkedin Ad Library platform reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown with endpoint summaries, command or API call guidance, task status, credit usage, result counts, and normalized findings or export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination status, incomplete-coverage notes, and references to raw JSONL exports when requested.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
