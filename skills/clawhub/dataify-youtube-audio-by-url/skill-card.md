## Description: <br>
Submits Dataify Builder jobs that collect YouTube audio files from one or more YouTube URLs and returns the task ID and status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to create Dataify YouTube audio collection tasks by URL, configure allowed audio settings, and receive task submission status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit credentialed external requests to Dataify using DATAIFY_API_TOKEN. <br>
Mitigation: Install only when Dataify YouTube audio task submission is expected, keep DATAIFY_API_TOKEN scoped to Dataify, and confirm token use before submission. <br>
Risk: Implicit invocation could submit an unintended YouTube URL or consume Dataify quota. <br>
Mitigation: Prefer explicit invocation and confirm the target URL, shared audio settings, and whether multiple URLs are intended before calling the Builder endpoint. <br>
Risk: Submitted tasks may involve external YouTube content and Dataify processing outside the local agent environment. <br>
Mitigation: Review the URL and Dataify account context before submission, and monitor Dataify quota and usage after task creation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-audio-by-url) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder?platform=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with parameter tables, shell command examples, and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task_id, status, submitted parameters, dashboard URL, and user-facing next steps after successful submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
