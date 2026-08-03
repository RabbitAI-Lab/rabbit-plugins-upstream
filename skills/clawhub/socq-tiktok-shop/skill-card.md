## Description: <br>
Research public TikTok Shop products, shops, creators, categories, and sales signals with SocQ. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to research public TikTok Shop entities, select SocQ endpoints, estimate credit use, run asynchronous collections, paginate results, and retrieve raw exports through the SocQ CLI, MCP, or REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SocQ API keys can be exposed if placed in prompts, query strings, committed files, or retained shell commands. <br>
Mitigation: Use the SOCQ_API_KEY environment variable or SocQ authentication flow, and avoid including credentials in prompts, URLs, or shell history. <br>
Risk: Large or repeated SocQ jobs may consume paid credits. <br>
Mitigation: Check account credits and endpoint billing before large requests, reduce result limits when scope is uncertain, and avoid blind retries of failed paid requests. <br>
Risk: Raw exports and task files come from an external paid service and may expire or need validation before use. <br>
Mitigation: Retrieve task files promptly, preserve task IDs for resumption, and report filters, collection time, partial coverage, and provider failures with results. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [TikTok Shop](references/platform.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline commands, API parameters, task status notes, and result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SocQ CLI, MCP, or REST execution guidance and references to task files or JSONL exports when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
