## Description: <br>
Collect Indeed job listings through the Dataify Scraper API from one or more Indeed job URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare Dataify collection tasks for Indeed job listings, confirm parameters with the user, and submit approved job URL collection requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit user-provided Indeed job URLs and collection parameters to Dataify for external processing. <br>
Mitigation: Review the Markdown confirmation table and proceed only after explicit user approval for the exact parameters. <br>
Risk: A Dataify API token is required and may be saved locally as DATAIFY_API_TOKEN. <br>
Mitigation: Save the token only with explicit user consent, do not echo it in user-facing output, and treat the environment variable as a secret. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-indeed-job-listings) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>
- [Dataify Scraper API builder endpoint](https://scraperapi.dataify.com/builder?platform=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown confirmation tables, shell command examples, and concise status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before real API calls and uses a Dataify API token from the user or DATAIFY_API_TOKEN.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
