## Description: <br>
Research public Instagram content, accounts, keywords, and performance data with SocQ through Instagram-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports using the SocQ CLI, MCP, or REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to research public Instagram accounts, posts, reels, hashtags, comments, transcripts, and performance data through SocQ while managing authentication, endpoint selection, asynchronous tasks, pagination, errors, and paid-credit limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public Instagram research can involve privacy-sensitive social data, especially follower lists, comments, transcripts, and exported raw files. <br>
Mitigation: Collect only public data supported by the selected endpoint, scope accounts, hashtags, dates, and result counts tightly, avoid unnecessary follower/comment/transcript collection, and follow applicable platform terms, privacy rules, and retention expectations. <br>
Risk: The SocQ integration uses a credit-metered API key, so large or repeated requests can consume paid credits or hit account limits. <br>
Mitigation: Check account credits before large jobs, inspect endpoint billing, reduce result limits when spend is not authorized, and do not blindly retry failed paid requests. <br>
Risk: Credential exposure could occur if the SocQ API key is placed in prompts, URLs, committed files, or retained shell commands. <br>
Mitigation: Store SOCQ_API_KEY in the process environment or SocQ auth configuration, avoid putting keys in MCP URLs or prompts, and avoid interactive shell commands that retain API keys in history. <br>
Risk: Asynchronous or paginated jobs may produce incomplete results if polling stops early, cursors are skipped, or provider failures are not reported. <br>
Mitigation: Poll tasks until succeeded or failed, preserve task IDs for resume, follow every required next_cursor, and report filters, collection time, partial coverage, and provider failures with the results. <br>


## Reference(s): <br>
- [SocQ Devtools Homepage](https://github.com/SocQAPI/socq-devtools) <br>
- [SocQ Instagram MCP Endpoint](https://api.socq.ai/mcp?platforms=instagram) <br>
- [Instagram Endpoint Selection](references/platform.md) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with CLI, MCP, and REST request details; may include JSON task results or raw JSONL export retrieval steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a SocQ account, SOCQ_API_KEY, and scoped public Instagram research requests; large or repeated requests may consume paid credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
