## Description: <br>
Research public Reddit content, accounts, keywords, and performance data with SocQ when an agent needs Reddit-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and research agents use this skill to collect public Reddit posts, comments, subreddit content, and keyword search results through SocQ while managing authentication, endpoint selection, credits, asynchronous task polling, pagination, and raw exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, Reddit URLs, task inputs, and raw exports are sent to SocQ. <br>
Mitigation: Avoid including secrets or private context in research inputs and use only public Reddit data supported by the selected endpoint. <br>
Risk: SocQ requests may consume paid credits, especially for broad or high-volume jobs. <br>
Mitigation: Check account credits and endpoint billing before large requests, reduce result limits when scope is unclear, and avoid retrying failed paid requests blindly. <br>
Risk: Asynchronous jobs can be duplicated or misreported if incomplete tasks, pagination, or provider failures are not handled. <br>
Mitigation: Preserve task IDs, poll until a terminal state, reuse idempotency keys for retries, follow next cursors, and report partial coverage or normalized errors. <br>
Risk: API keys can be exposed through prompts, query strings, committed files, or shell history. <br>
Mitigation: Use SOCQ_API_KEY or SocQ auth storage, avoid embedding keys in MCP URLs or retained commands, and clear credentials when access is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-reddit-research) <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [SocQ Reddit MCP Server](https://api.socq.ai/mcp?platforms=reddit) <br>
- [Reddit Platform Reference](references/platform.md) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [SocQ Reddit Comments API](https://docs.socq.ai/api-manual/reddit/comments) <br>
- [SocQ Reddit Posts API](https://docs.socq.ai/api-manual/reddit/posts) <br>
- [SocQ Reddit Search API](https://docs.socq.ai/api-manual/reddit/search) <br>
- [SocQ Reddit Subreddit Posts API](https://docs.socq.ai/api-manual/reddit/subreddit-posts) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Configuration, Files] <br>
**Output Format:** [Markdown guidance with CLI, MCP, and REST examples plus optional JSONL exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include task IDs, filters used, collection timing, partial coverage notes, provider failure summaries, pagination cursors, and raw task files when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
