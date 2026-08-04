## Description: <br>
Research public Reddit content, accounts, keywords, and performance data with SocQ through CLI, MCP, or REST workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect and analyze public Reddit posts, comments, subreddit activity, and keyword search results with SocQ. It helps agents choose endpoints, estimate credit use, run asynchronous tasks, paginate results, and report collection limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A SocQ API key could be exposed through prompts, URLs, shell history, logs, or committed files. <br>
Mitigation: Store SOCQ_API_KEY in the process environment or SocQ local config, avoid command-line API-key flags during interactive use, and never include keys in MCP URLs or retained text. <br>
Risk: Large or repeated Reddit collection jobs may consume paid credits or exceed API-key credit limits. <br>
Mitigation: Check account credits before large requests, inspect endpoint billing, reduce result limits when scope is not authorized, and avoid blind retries after paid failures. <br>
Risk: Results can be incomplete when pagination stops early, a provider fails, or requested filters are unsupported. <br>
Mitigation: Follow every required next_cursor, preserve task IDs for resumed polling, and report filters, collection time, partial coverage, and provider failures with the results. <br>


## Reference(s): <br>
- [SocQ ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-reddit-research) <br>
- [SocQ Publisher Profile](https://clawhub.ai/user/socq) <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [Hosted SocQ Reddit MCP](https://api.socq.ai/mcp?platforms=reddit) <br>
- [Reddit Platform Reference](references/platform.md) <br>
- [Authentication Reference](references/authentication.md) <br>
- [Billing and Cost Control Reference](references/billing.md) <br>
- [Asynchronous Tasks Reference](references/async-tasks.md) <br>
- [Pagination and Files Reference](references/pagination.md) <br>
- [Errors and Recovery Reference](references/errors.md) <br>
- [Reddit Comments API](https://docs.socq.ai/api-manual/reddit/comments) <br>
- [Reddit Posts API](https://docs.socq.ai/api-manual/reddit/posts) <br>
- [Reddit Search API](https://docs.socq.ai/api-manual/reddit/search) <br>
- [Reddit Subreddit Posts API](https://docs.socq.ai/api-manual/reddit/subreddit-posts) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline commands and API request details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task IDs, endpoint choices, filters, collection time, pagination status, partial coverage, provider failures, and raw JSONL export retrieval guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
