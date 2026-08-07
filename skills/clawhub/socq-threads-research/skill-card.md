## Description: <br>
Research public Threads content, accounts, keywords, and performance data with SocQ through CLI, MCP, or REST workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to select SocQ Threads endpoints, configure authentication, estimate credit usage, run asynchronous public-data collection, handle pagination, and retrieve normalized or raw exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SocQ requests require an API key and network access to an external service. <br>
Mitigation: Use SOCQ_API_KEY from the process environment and avoid placing credentials in prompts, query strings, committed files, or retained shell commands. <br>
Risk: Large or repeated requests may consume paid SocQ credits. <br>
Mitigation: Check account balance and endpoint billing before large jobs, reduce result limits when scope is uncertain, and ask for authorization before expanding spend. <br>
Risk: Network retries or failed asynchronous jobs can create duplicate paid work if resubmitted blindly. <br>
Mitigation: Use reusable idempotency keys for retryable submissions, preserve task IDs, poll incomplete tasks, and inspect normalized errors before retrying. <br>
Risk: Results may be incomplete when pagination stops early, providers fail, or requested filters are unsupported. <br>
Mitigation: Follow next_cursor values until the requested cap or end of results, validate endpoint schemas, and report filters, collection time, partial coverage, and provider failures. <br>


## Reference(s): <br>
- [SocQ Developer Tools](https://github.com/SocQAPI/socq-devtools) <br>
- [SocQ Threads MCP Server](https://api.socq.ai/mcp?platforms=threads) <br>
- [Threads Posts API](https://docs.socq.ai/api-manual/threads/posts) <br>
- [Threads Profiles API](https://docs.socq.ai/api-manual/threads/profiles) <br>
- [Threads User Posts API](https://docs.socq.ai/api-manual/threads/user-posts) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [Threads](references/platform.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands, MCP or REST request details, and data-collection summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference task IDs, cursors, filters, collection time, partial coverage, provider failures, and raw JSONL export retrieval when relevant.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
