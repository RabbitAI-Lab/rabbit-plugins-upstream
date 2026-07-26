## Description: <br>
Submits user-directed YouTube profile collection jobs to Dataify Builder in URL or keyword mode and returns the task ID, status, and dashboard link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to configure and submit Dataify YouTube profile collection jobs by channel URL or search keyword. It helps confirm parameters, reuse a Dataify API TOKEN, submit the Builder request, and report the resulting task details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use DATAIFY_API_TOKEN to submit selected YouTube URLs or keywords to Dataify. <br>
Mitigation: Review the collection mode, URLs or keywords, page count, and file name before authorizing a run. <br>
Risk: A missing or mishandled Dataify API TOKEN can block submission or expose credentials. <br>
Mitigation: Prefer the DATAIFY_API_TOKEN environment variable or secure local secret handling, and do not run the Builder request without an intended token. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-profiles) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task_id, status, selected mode, parameters, file_name, dashboard_url, and a short completion message after successful submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
