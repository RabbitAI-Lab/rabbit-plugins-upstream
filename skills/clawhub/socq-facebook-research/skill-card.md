## Description: <br>
Research public Facebook content, accounts, keywords, and performance data with SocQ through endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports via CLI, MCP, or REST. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to guide agents through public Facebook research with SocQ, including endpoint selection, authenticated execution, credit control, asynchronous task tracking, pagination, and result reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Facebook targets, including URLs, usernames, IDs, and search queries, are sent to SocQ during use. <br>
Mitigation: Use SocQ only for authorized public-data research, avoid sensitive investigative targets, and configure scoped API keys with IP, rate, and credit limits where possible. <br>
Risk: Large or repeated requests can consume paid SocQ credits. <br>
Mitigation: Check account credits, inspect endpoint billing, reduce result limits when spend is not authorized, and do not retry failed paid requests blindly. <br>
Risk: Incomplete pagination, provider failures, or unsupported filters can make results partial. <br>
Mitigation: Poll tasks to completion, follow next_cursor until the requested cap or completion, and report filters, collection time, partial coverage, and provider failures. <br>


## Reference(s): <br>
- [SocQ Facebook Research on ClawHub](https://clawhub.ai/socq/skills/socq-facebook-research) <br>
- [SocQ publisher profile](https://clawhub.ai/user/socq) <br>
- [SocQ devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [Hosted SocQ Facebook MCP server](https://api.socq.ai/mcp?platforms=facebook) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Facebook Endpoint Selection](references/platform.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands, API parameters, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SocQ task IDs, pagination cursors, filters, coverage notes, credit checks, and raw JSONL export retrieval instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
