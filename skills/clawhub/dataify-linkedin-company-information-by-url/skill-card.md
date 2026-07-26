## Description: <br>
Prepare Dataify builder requests for the linkedin.com scraper family rooted at linkedin_company_information_by-url, including tool selection, saved parameter lookup, and generation of a scraperapi.dataify.com/builder curl request using DATAIFY_API_TOKEN. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to prepare Dataify builder requests for LinkedIn company and job scraping tools. It guides tool selection, parameter collection, and curl command generation for the Dataify builder API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DATAIFY_API_TOKEN may be exposed if copied into logs, shell history, or shared command output. <br>
Mitigation: Keep DATAIFY_API_TOKEN private, prefer a secure secret store or carefully protected environment variable, and avoid pasting token values directly into shared commands. <br>
Risk: The generated curl command sends the API token and supplied parameters to Dataify. <br>
Mitigation: Review the generated curl command and parameter values before running it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-linkedin-company-information-by-url) <br>
- [Publisher profile](https://clawhub.ai/user/dataify-server) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify builder endpoint](https://scraperapi.dataify.com/builder) <br>
- [Tool parameter catalog](references/tool-params.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated curl commands use DATAIFY_API_TOKEN from the environment and include Dataify spider_name, spider_id, spider_parameters, spider_errors, and file_name fields.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
