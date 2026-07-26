## Description: <br>
Submits user-reviewed Dataify Builder tasks to collect Facebook post comments from Facebook post URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to review Facebook comment collection parameters, resolve a Dataify API TOKEN, and submit Dataify Builder jobs for one or more Facebook post URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use a saved DATAIFY_API_TOKEN and create external Dataify tasks. <br>
Mitigation: Review the Facebook URL, collection limits, and file name before submission, and do not call the Builder endpoint without an API TOKEN. <br>
Risk: Incorrect parameters can submit the wrong collection job or fail validation. <br>
Mitigation: Confirm the parameter table first, require Facebook URLs to start with https://www.facebook.com/, and use only the documented dropdown values and non-negative limits. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-facebook-comment-by-url) <br>
- [dataify-server publisher profile](https://clawhub.ai/user/dataify-server) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API calls, Configuration guidance, JSON] <br>
**Output Format:** [Markdown parameter tables and instructions, optional shell commands, and JSON task summaries from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Submits form-encoded Dataify Builder requests and returns task_id, status, parameters, file_name, dashboard_url, and message when the helper script succeeds.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
