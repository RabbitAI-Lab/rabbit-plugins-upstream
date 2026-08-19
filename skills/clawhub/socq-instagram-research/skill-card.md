## Description:

Research public Instagram content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to collect, paginate, and summarize public Instagram profiles, posts, reels, comments, hashtags, transcripts, and related performance data through SocQ.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for MCP, CLI, or REST requests.

Mitigation: Keep SOCQ_API_KEY in the environment or local SocQ auth, and do not place API keys in prompts, URLs, shell history, or project files.

Risk: SocQ requests can spend credits, especially for large-volume or multi-endpoint Instagram collection.

Mitigation: Check account balance and endpoint billing before large jobs, use small result caps for exploratory runs, and get user confirmation before paid large-volume work.

Risk: Asynchronous tasks may still be queued or running after submission.

Mitigation: Preserve task IDs, poll until a terminal status, and avoid resubmitting duplicate work when a task is incomplete or temporarily unavailable.

Risk: Pagination, provider failures, unsupported filters, or early stops can make coverage incomplete.

Mitigation: Report result counts, pages read, remaining data, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

## Reference(s):

- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Instagram API documentation](https://docs.socq.ai/api-manual/instagram)
- [SocQ Instagram platform page](https://socq.ai/apis/instagram)
- [SocQ MCP and CLI overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Instagram endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, command examples, task status, credit usage, result counts, normalized findings, and raw export locations when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination status, incomplete coverage notes, and unsupported filter notes.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
