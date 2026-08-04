## Description: <br>
Research public Pinterest content, accounts, keywords, and performance data with SocQ through CLI, MCP, or REST workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to collect and analyze public Pinterest pins, profiles, search results, and user pins through SocQ while managing endpoint selection, authentication, credits, asynchronous tasks, pagination, and raw exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SocQ API keys can be exposed if placed in prompts, query strings, committed files, or retained shell commands. <br>
Mitigation: Use SOCQ_API_KEY or SocQ login storage, avoid command-line API keys during interactive use, and never commit or retain credentials. <br>
Risk: Broad SocQ jobs may consume paid credits or run into account credit ceilings. <br>
Mitigation: Check credits before large requests, reduce result limits when spend is not authorized, and use representative test requests before broad collection. <br>
Risk: Pinterest results may be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported. <br>
Mitigation: Follow every next_cursor needed for the requested scope and report filters, collection time, partial coverage, and provider failures with the results. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [Pinterest Platform Reference](references/platform.md) <br>
- [Pinterest Pins API](https://docs.socq.ai/api-manual/pinterest/pins) <br>
- [Pinterest Profiles API](https://docs.socq.ai/api-manual/pinterest/profiles) <br>
- [Pinterest Search API](https://docs.socq.ai/api-manual/pinterest/search) <br>
- [Pinterest User Pins API](https://docs.socq.ai/api-manual/pinterest/user-pins) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with SocQ CLI, MCP, REST, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task IDs, filters, collection time, partial coverage notes, provider failures, pagination status, and raw JSONL export guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
