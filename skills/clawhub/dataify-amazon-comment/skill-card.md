## Description: <br>
Submits Amazon product review collection tasks by URL through Dataify Builder and returns the resulting task_id. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to confirm Amazon product review collection parameters, submit a Dataify Builder job, and receive a task_id for later review in Dataify. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Dataify API TOKEN and can create Dataify Builder tasks. <br>
Mitigation: Confirm the Amazon URL and file_name before submission, and only persist DATAIFY_API_TOKEN when storing that credential in the user environment is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-amazon-comment) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown guidance and parameter tables with optional shell commands; the helper script prints a JSON task summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Dataify API TOKEN, confirms the Amazon URL and file_name before submission, and returns task_id, dashboard_url, and message when the Builder task is created.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
