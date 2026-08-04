## Description: <br>
Research public YouTube content, accounts, keywords, and performance data with SocQ. Use when an agent needs YouTube-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent operators use this skill to plan and run public YouTube research through SocQ, including endpoint selection, credential setup, credit checks, asynchronous task polling, pagination, and raw export retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SOCQ_API_KEY for CLI, MCP, or REST access. <br>
Mitigation: Provide the key through the environment and avoid placing it in prompts, query strings, committed files, or retained shell commands. <br>
Risk: SocQ is credit-metered and large YouTube jobs may consume paid credits. <br>
Mitigation: Check account credits and endpoint billing before large requests, reduce scope when spend is not authorized, and submit one representative request first when input quality is uncertain. <br>
Risk: Public YouTube collections can be incomplete when tasks are unfinished, pagination stops early, provider failures occur, or filters are unsupported. <br>
Mitigation: Poll tasks to completion, follow pagination for the requested scope, and report filters, collection time, partial coverage, and normalized provider failures. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [Hosted SocQ YouTube MCP endpoint](https://api.socq.ai/mcp?platforms=youtube) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [YouTube Endpoint Reference](references/platform.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, API request examples, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task IDs, pagination cursors, credit estimates, raw export guidance, and caveats about partial coverage.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
