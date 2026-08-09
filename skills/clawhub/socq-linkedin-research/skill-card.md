## Description: <br>
Research public LinkedIn content, accounts, keywords, and performance data with SocQ. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to select SocQ LinkedIn endpoints, configure authentication, estimate credit use, run asynchronous public LinkedIn data collection, paginate results, and retrieve raw exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkedIn research targets and related query inputs are sent to SocQ as an external service. <br>
Mitigation: Use only public, approved research inputs and confirm SocQ is approved for the organization's data handling needs. <br>
Risk: Requests may consume paid SocQ credits. <br>
Mitigation: Check account balance, endpoint billing, result limits, and API key credit caps before large jobs. <br>
Risk: API keys can be exposed through prompts, query strings, command history, or committed files. <br>
Mitigation: Prefer environment-based credentials, avoid putting keys in MCP URLs or retained shell commands, and clear credentials when they are no longer needed. <br>
Risk: Results can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported. <br>
Mitigation: Report filters, collection time, pagination status, partial coverage, and provider failures with the results. <br>


## Reference(s): <br>
- [SocQ LinkedIn Research on ClawHub](https://clawhub.ai/socq/skills/socq-linkedin-research) <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [SocQ LinkedIn MCP Server](https://api.socq.ai/mcp?platforms=linkedin) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [LinkedIn Platform Reference](references/platform.md) <br>
- [SocQ LinkedIn Companies API](https://docs.socq.ai/api-manual/linkedin/companies) <br>
- [SocQ LinkedIn Jobs API](https://docs.socq.ai/api-manual/linkedin/jobs) <br>
- [SocQ LinkedIn Posts API](https://docs.socq.ai/api-manual/linkedin/posts) <br>
- [SocQ LinkedIn Profiles API](https://docs.socq.ai/api-manual/linkedin/profiles) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, text] <br>
**Output Format:** [Markdown with CLI, MCP, and REST request guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include endpoint selections, credit estimates, filters, task IDs, pagination status, partial coverage notes, provider failures, and raw JSONL export retrieval guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
