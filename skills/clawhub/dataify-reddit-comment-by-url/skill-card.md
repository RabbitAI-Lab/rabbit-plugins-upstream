## Description: <br>
Submits Dataify Reddit Post Comment by URL Builder tasks for collecting Reddit post comments by URL and helps configure or troubleshoot the required Dataify API TOKEN. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to review parameters, submit Reddit comment collection jobs to Dataify Builder, and receive the resulting task ID, status, and dashboard link. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reddit URLs and task settings are sent to Dataify using the user's API TOKEN. <br>
Mitigation: Review the parameter table before submission and install or invoke the skill only when Dataify Reddit comment collection is intended. <br>
Risk: A Dataify API TOKEN is required for submission. <br>
Mitigation: Use DATAIFY_API_TOKEN for saved local use, do not submit without a token, and do not persist a provided token unless the user confirms. <br>
Risk: Submitting with incorrect parameters can create the wrong Dataify collection job. <br>
Mitigation: Confirm required and optional values before execution, validate Reddit URLs and non-negative numeric limits, and report the returned task_id and status. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-reddit-comment-by-url) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown parameter confirmations, shell command examples, and JSON task submission summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports spider_id, task_id, status, submitted parameters, file_name, dashboard_url, and a user-facing message after successful submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
