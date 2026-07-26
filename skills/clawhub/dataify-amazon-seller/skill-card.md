## Description: <br>
Submits Dataify Builder tasks for Amazon seller information collection by URL, returns the created task_id, and helps configure or reuse the DATAIFY_API_TOKEN credential. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit Amazon seller URL collection jobs through Dataify Builder and receive the resulting task_id. It also guides API TOKEN setup, parameter confirmation, and basic troubleshooting for Dataify Builder request failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DATAIFY_API_TOKEN is a sensitive credential that may be exposed if copied into shared prompts, logs, or persistent shell configuration. <br>
Mitigation: Treat the token as secret, prefer session-scoped storage when practical, and avoid sharing command history or environment files containing the token. <br>
Risk: Submitting an unintended Amazon seller URL or file_name can create unwanted Dataify account activity. <br>
Mitigation: Review the confirmation table for url and file_name before allowing submission. <br>
Risk: The external Builder request can fail because of an invalid token, malformed parameters, network errors, or a response without task_id. <br>
Mitigation: Validate the token and required fields before submission, and only report success after reading data.task_id from the Builder response. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-amazon-seller) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify Builder Endpoint](https://scraperapi.dataify.com/builder) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with parameter tables, shell command examples, and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task_id, url, file_name, dashboard_url, and a status message after successful submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
