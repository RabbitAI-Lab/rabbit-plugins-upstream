## Description: <br>
Submits Dataify Builder tasks that collect Facebook post data from one or more Facebook post URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure a Dataify API TOKEN, confirm Facebook post URL parameters, submit Dataify Builder jobs, and receive the resulting task ID and status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use a saved DATAIFY_API_TOKEN and send selected Facebook post URL parameters to Dataify. <br>
Mitigation: Install only when this Dataify submission behavior is intended, review the parameter confirmation before submission, and avoid saving the token on shared machines unless future reuse is acceptable. <br>
Risk: A default Facebook post URL can be used if the user does not provide a URL after parameter confirmation. <br>
Mitigation: Confirm or replace the URL before running the task, especially when collecting multiple posts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-facebook-post-by-url) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful submissions return spider_id, task_id, status, parameters, file_name, dashboard_url, and message.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
