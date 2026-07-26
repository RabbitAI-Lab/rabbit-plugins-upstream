## Description: <br>
Submit Dataify YouTube video file collection jobs by URL and return the created task ID, status, parameters, dashboard URL, and completion message. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to submit Dataify Builder tasks that collect YouTube video files from one or more YouTube URLs. It helps configure allowed media settings, validate inputs, submit the Builder request with a Dataify API TOKEN, and report the resulting task metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Dataify API TOKEN and may submit jobs under the user's Dataify account. <br>
Mitigation: Confirm the token source before submission, do not persist tokens without user confirmation, and avoid calling the Builder endpoint when no token is available. <br>
Risk: YouTube URLs and selected collection settings are sent to Dataify. <br>
Mitigation: Review the parameter confirmation table before running the task and avoid submitting sensitive or unintended URLs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-video-by-url) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown parameter tables and instructions, with JSON task summaries from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task_id, status, submitted parameters, shared video settings, file_name, dashboard_url, and message after successful submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
