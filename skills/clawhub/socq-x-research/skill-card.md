## Description: <br>
Research public X content, accounts, keywords, and performance data with SocQ. Use when an agent needs X-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to plan and run public X research with SocQ, including endpoint selection, credential setup, asynchronous task handling, pagination, and reporting of coverage or provider failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SocQ requests require SOCQ_API_KEY, and careless handling could expose credentials. <br>
Mitigation: Set the key in the process environment, avoid prompts, query strings, committed files, and retained shell commands, and use account or key controls such as IP allowlists and spending limits where available. <br>
Risk: Large or repeated collection jobs may consume paid SocQ credits. <br>
Mitigation: Check account credits and endpoint billing before large requests, reduce result limits when spend is not authorized, and review large collection scopes before execution. <br>
Risk: X search, trends, pagination, and provider behavior can produce partial or time-sensitive coverage. <br>
Mitigation: Report collection time, filters, pagination status, unsupported filters, and provider failures, and avoid claiming exhaustive coverage when the skill evidence does not support it. <br>
Risk: Blind retries after failures can duplicate work or paid requests. <br>
Mitigation: Inspect normalized errors first, reuse idempotency keys for transport retries, preserve task IDs, and resume polling rather than resubmitting incomplete tasks. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [Hosted SocQ X MCP server](https://api.socq.ai/mcp?platforms=x) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [X Platform Reference](references/platform.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCQ_API_KEY and may initiate credit-metered SocQ CLI, MCP, or REST requests when used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
