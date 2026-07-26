## Description: <br>
Turns a user's Google Jobs search request into a confirmed Dataify Scraper API form POST and returns the raw response body. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search Google Jobs through the Dataify Scraper API after reviewing a pre-call parameter table and confirming the request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed job search parameters and the Dataify API token are sent to Dataify. <br>
Mitigation: Use the required preview table to confirm only intended parameters, and avoid entering unrelated sensitive data in job search fields. <br>
Risk: A mistaken parameter value could cause an unintended Google Jobs query or bypass cached results. <br>
Mitigation: Review every field in the pre-call confirmation table and regenerate it after any requested change before approving the API call. <br>


## Reference(s): <br>
- [Dataify Google Jobs API reference](references/google_jobs_api.md) <br>
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request) <br>
- [ClawHub dataify-google-jobs release page](https://clawhub.ai/dataify-server/skills/dataify-google-jobs) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API Calls, Text] <br>
**Output Format:** [Markdown confirmation table followed by the raw Dataify API response body, typically JSON or HTML depending on the json parameter.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before the API call and uses a Dataify API token for authentication.] <br>

## Skill Version(s): <br>
1.2.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
