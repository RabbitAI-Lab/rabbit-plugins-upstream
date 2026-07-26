## Description: <br>
Submits Dataify YouTube Comment by Video ID Builder tasks for collecting YouTube comment information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and users use this skill to submit Dataify Builder jobs for collecting YouTube comments by video ID, confirm the task parameters, and receive the resulting task ID and status. It supports single or multiple video parameter groups and directs users to Dataify to view or manage results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Dataify API TOKEN to create Builder tasks. <br>
Mitigation: Use the token only for trusted runs, provide it explicitly or via DATAIFY_API_TOKEN, and save it locally only after user confirmation. <br>
Risk: The skill creates Dataify Builder tasks for YouTube video IDs the user confirms. <br>
Mitigation: Review the parameter table before submission and submit only video IDs and collection counts the user intends to process. <br>
Risk: Users may expect the task response to contain collected comments. <br>
Mitigation: Treat the response as task metadata only and use the Dataify dashboard to view or manage results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-comment-by-id) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder?platform=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance and optional JSON summary from the bundled script] <br>
**Output Parameters:** [YouTube video ID groups, load_replies, num_of_comments, file_name, and DATAIFY_API_TOKEN] <br>
**Other Properties Related to Output:** [Returns task_id, status, submitted parameters, file_name, dashboard_url, and message; it does not return collected YouTube comments.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
