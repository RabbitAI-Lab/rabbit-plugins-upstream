## Description: <br>
Research public Facebook content, accounts, keywords, and performance data with SocQ. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and research teams use this skill to collect and analyze public Facebook entities, posts, comments, events, profiles, reels, transcripts, and related performance data through SocQ. It helps agents choose endpoints, estimate credit usage, run asynchronous jobs, paginate results, and retrieve raw exports while reporting collection limits and provider failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses SocQ as an external paid service, so Facebook research requests and collected public results are processed outside the agent runtime. <br>
Mitigation: Confirm the user is comfortable with SocQ processing before use, collect only public supported data, and report filters, collection time, partial coverage, and provider failures with results. <br>
Risk: Requests may consume paid SocQ credits and large result volumes can increase cost. <br>
Mitigation: Check account credits before large jobs, set credit limits where possible, inspect endpoint billing, reduce result limits when spend is not authorized, and avoid blind retries after failed paid requests. <br>
Risk: A SOCQ_API_KEY is required and could be exposed if placed in prompts, URLs, committed files, or shell history. <br>
Mitigation: Use the process environment or local SocQ auth configuration, avoid query-string credentials and retained shell commands, and rely on API-key IP allowlists, rate limits, or credit ceilings where available. <br>
Risk: Asynchronous tasks, pagination, provider failures, or unsupported filters can produce incomplete or misleading results if treated as complete collections. <br>
Mitigation: Poll tasks until succeeded or failed, preserve task IDs, follow every required next_cursor, validate endpoint schemas after errors, and avoid claiming completeness when pagination ends early or providers fail. <br>


## Reference(s): <br>
- [SocQ developer tools homepage](https://github.com/SocQAPI/socq-devtools) <br>
- [Hosted SocQ Facebook MCP server](https://api.socq.ai/mcp?platforms=facebook) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [Facebook](references/platform.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline CLI, MCP, and REST request details plus links to raw JSONL exports when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference asynchronous task IDs, pagination cursors, selected filters, collection time, partial coverage, provider failures, credit estimates, and SocQ raw export files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
