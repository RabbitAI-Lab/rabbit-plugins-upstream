## Description: <br>
Submits Dataify Instagram Profile Builder tasks for collecting Instagram profiles by username or profile URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit Instagram profile collection jobs to Dataify Builder, choose username or profile URL mode, validate parameters, and receive the created task ID and status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send Instagram usernames or profile URLs to Dataify and create external collection jobs. <br>
Mitigation: Use it only when the user intends to submit those Dataify jobs, confirm the selected collection mode and parameters before execution, and stop after reporting the task ID and status. <br>
Risk: A locally saved DATAIFY_API_TOKEN can be reused for later Builder submissions. <br>
Mitigation: Do not save tokens silently; ask before providing save commands and avoid local persistence unless it matches the user's security practices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-instagram-profiles) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder?platform=1) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with shell commands and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May submit Dataify Builder requests using DATAIFY_API_TOKEN and returns mode, spider_id, task_id, status, parameters, file_name, dashboard_url, and message.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
