## Description: <br>
Prepare Dataify builder requests for the glassdoor.com scraper family rooted at glassdoor_company_by-url, including tool selection, saved parameter options, and an authenticated curl request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to prepare authenticated Dataify builder requests for Glassdoor company and job-listing scraper tools, choosing one tool and supplying or normalizing parameter values before running a curl request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitting scraper parameters and API requests sends user-provided inputs to Dataify. <br>
Mitigation: Confirm Dataify is trusted for the intended inputs before running generated requests. <br>
Risk: Persistently storing DATAIFY_API_TOKEN in shell startup files can increase credential exposure. <br>
Mitigation: Prefer a session-scoped token or credential manager, and review the generated curl command before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-glassdoor-company-by-url) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify Builder Endpoint](https://scraperapi.dataify.com/builder) <br>
- [Tool Parameter Catalog](references/tool-params.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with curl command blocks and JSON parameter payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided DATAIFY_API_TOKEN and selected Glassdoor tool parameters.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
