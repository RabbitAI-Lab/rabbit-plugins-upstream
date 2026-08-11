## Description: <br>
Research public Marketplace listings, sellers, prices, and product details with SocQ. Use when an agent needs Facebook Marketplace-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to plan and execute public Facebook Marketplace research through SocQ, including endpoint selection, asynchronous collection, pagination, billing checks, and result reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SocQ API key for CLI, MCP, and REST requests. <br>
Mitigation: Use SOCQ_API_KEY from the process environment and avoid placing keys in prompts, query strings, committed files, or retained shell commands. <br>
Risk: SocQ is a credit-metered service, so large or repeated collection jobs may consume paid credits. <br>
Mitigation: Check account credits and endpoint billing before large requests, reduce scope when spend is not authorized, and avoid blind retries of failed paid requests. <br>
Risk: Marketplace results may be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported. <br>
Mitigation: Follow next_cursor until the requested cap or completion, preserve task IDs for recovery, and report filters, collection time, partial coverage, and provider failures with the results. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [Facebook Marketplace Item API](https://docs.socq.ai/api-manual/facebook-marketplace/item) <br>
- [Facebook Marketplace Location Search API](https://docs.socq.ai/api-manual/facebook-marketplace/location-search) <br>
- [Facebook Marketplace Search API](https://docs.socq.ai/api-manual/facebook-marketplace/search) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [Facebook Marketplace](references/platform.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SocQ task IDs, pagination cursors, cost notes, partial-coverage notes, and raw JSONL export guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
