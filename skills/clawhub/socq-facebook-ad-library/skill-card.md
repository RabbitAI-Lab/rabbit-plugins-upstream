## Description: <br>
Research public ads, advertisers, creatives, and campaign activity with SocQ through Facebook Ad Library-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to plan and run SocQ workflows for researching public Facebook Ad Library ads, advertisers, creatives, and campaign activity. It helps select endpoints, configure authentication, estimate credit use, execute asynchronous jobs, handle pagination, and retrieve raw exports when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SocQ is an external paid service, so requests may consume credits and send requested public Facebook Ad Library queries to SocQ. <br>
Mitigation: Check account credits before large jobs, set reasonable credit limits, reduce scope when spend is not authorized, and submit representative small requests when input quality is uncertain. <br>
Risk: The skill requires SOCQ_API_KEY authentication, and leaked keys could expose account access or paid usage. <br>
Mitigation: Keep API keys in the process environment or local SocQ configuration, and do not place keys in prompts, URLs, committed files, or retained shell commands. <br>
Risk: Provider failures, unsupported filters, or early pagination stops can make collected Facebook Ad Library results incomplete. <br>
Mitigation: Report selected filters, collection time, pagination status, partial coverage, and provider failures; do not claim completeness when the workflow stops early or a requested filter is unsupported. <br>
Risk: Blindly retrying failed paid requests can duplicate work or consume unnecessary credits. <br>
Mitigation: Inspect normalized errors before retrying, preserve task IDs for resumption, and reuse idempotency keys for transport retries. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [SocQ Facebook Ad Library MCP Server](https://api.socq.ai/mcp?platforms=facebook-ad-library) <br>
- [Facebook Ad Library Ad API](https://docs.socq.ai/api-manual/facebook-ad-library/ad) <br>
- [Facebook Ad Library Company Ads API](https://docs.socq.ai/api-manual/facebook-ad-library/company-ads) <br>
- [Facebook Ad Library Company Search API](https://docs.socq.ai/api-manual/facebook-ad-library/company-search) <br>
- [Facebook Ad Library Search API](https://docs.socq.ai/api-manual/facebook-ad-library/search) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [Facebook Ad Library](references/platform.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with CLI, MCP, and REST examples; result workflows may reference JSON or JSONL outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected filters, collection time, task IDs, pagination status, partial coverage, provider failures, and credit or billing notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
