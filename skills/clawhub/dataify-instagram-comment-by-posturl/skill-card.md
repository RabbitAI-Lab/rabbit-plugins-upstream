## Description: <br>
Submits Dataify Builder jobs that collect Instagram post comments from one or more post URLs and returns the resulting task ID and status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers with a Dataify account use this skill to submit Instagram post comment collection jobs by post URL, including multi-post submissions, and receive the task ID and status for follow-up in Dataify. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill submits task parameters to Dataify under the user's account. <br>
Mitigation: Review post URLs and task settings before submission, and submit only when the user intends to create a Dataify collection job. <br>
Risk: A saved Dataify API TOKEN can be reused for future submissions. <br>
Mitigation: Use DATAIFY_API_TOKEN deliberately, do not persist tokens silently, and ask for confirmation before providing save commands. <br>
Risk: Incorrect or out-of-scope post URLs could submit unintended collection targets. <br>
Mitigation: Validate that each posturl is non-empty and starts with https://www.instagram.com/ before calling the Builder endpoint. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-instagram-comment-by-posturl) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder?platform=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with parameter tables, shell commands, and JSON task summaries from the helper script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Dataify API TOKEN and one or more Instagram post URLs; the helper script prints spider_id, task_id, status, parameters, file_name, dashboard_url, and message.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
