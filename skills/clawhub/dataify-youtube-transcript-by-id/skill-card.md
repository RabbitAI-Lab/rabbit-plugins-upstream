## Description: <br>
Dataify YouTube Transcript By ID submits Dataify Builder jobs to collect YouTube subtitles or transcripts by video ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and submit YouTube transcript collection jobs through Dataify, then receive the task ID, status, and dashboard guidance for managing results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a saved DATAIFY_API_TOKEN to submit Dataify Builder jobs. <br>
Mitigation: Review parameters before submission and save the token locally only when future reuse is intended. <br>
Risk: Submitted jobs send YouTube video IDs and subtitle settings to Dataify for processing. <br>
Mitigation: Confirm the video IDs, subtitle language, subtitle type, selected-only setting, and file name before creating the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-transcript-by-id) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown parameter tables, command examples, and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task_id, status, submitted parameters, dashboard URL, and guidance after successful task creation; it does not return transcript files.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
