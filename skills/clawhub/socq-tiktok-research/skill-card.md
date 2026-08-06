## Description: <br>
Research public TikTok content, accounts, keywords, and performance data with SocQ through endpoint selection, authenticated CLI, MCP, or REST execution, credit checks, asynchronous task handling, pagination, and raw exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to collect and analyze public TikTok content through SocQ's CLI, MCP server, or REST API. It supports endpoint selection, authenticated requests, cost checks, asynchronous task polling, pagination, and raw export retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SocQ API key for CLI, MCP, and REST requests. <br>
Mitigation: Keep SOCQ_API_KEY in the process environment or local SocQ configuration, and avoid placing keys in prompts, URLs, committed files, or retained shell commands. <br>
Risk: SocQ is an external, credit-metered service, and large collections may consume paid credits. <br>
Mitigation: Check account credits and endpoint billing before large jobs, reduce requested volume when cost is unclear, and avoid retrying failed paid requests blindly. <br>
Risk: Asynchronous tasks, pagination, provider failures, or unsupported filters can produce incomplete collections. <br>
Mitigation: Poll tasks to a terminal state, follow every required next_cursor, preserve task IDs for resumption, and report filters, collection time, partial coverage, and provider failures. <br>
Risk: Results and raw exports are handled through SocQ's external service. <br>
Mitigation: Collect only public data supported by the selected endpoint, retrieve expiring file URLs promptly, and avoid treating raw provider files as normalized data unless documented. <br>


## Reference(s): <br>
- [SocQ Developer Tools](https://github.com/SocQAPI/socq-devtools) <br>
- [SocQ TikTok MCP Server](https://api.socq.ai/mcp?platforms=tiktok) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [TikTok Endpoint Reference](references/platform.md) <br>
- [SocQ TikTok Comments API](https://docs.socq.ai/api-manual/tiktok/comments) <br>
- [SocQ TikTok Search API](https://docs.socq.ai/api-manual/tiktok/search) <br>
- [SocQ TikTok Profiles API](https://docs.socq.ai/api-manual/tiktok/profiles) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline commands, API request details, configuration notes, and result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SocQ task IDs, filters, collection timing, partial coverage notes, provider failure notes, and raw JSONL export retrieval guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
