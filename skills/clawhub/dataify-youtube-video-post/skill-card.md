## Description: <br>
Guides agents through Dataify Builder submissions for collecting YouTube video posts by URL, search filters, hashtag, podcast URL, keyword, or Explore URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to choose a YouTube video collection mode, validate parameters, submit a Dataify Builder task with a Dataify API TOKEN, and receive the task ID and status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends DATAIFY_API_TOKEN as a bearer credential to Dataify for Builder requests. <br>
Mitigation: Use the skill only for intended Dataify collection tasks, treat DATAIFY_API_TOKEN as a credential, and review token handling before execution. <br>
Risk: The skill submits user-selected YouTube collection parameters to Dataify and creates external collection jobs. <br>
Mitigation: Review the selected mode, URLs, filters, counts, and file name before submitting the Builder request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-video-post) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify Builder API endpoint](https://scraperapi.dataify.com/builder?platform=1) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, JSON] <br>
**Output Format:** [Markdown guidance with optional shell commands and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns mode, spider_id, task_id, status, parameters, file_name, dashboard_url, and message after a successful Builder submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
