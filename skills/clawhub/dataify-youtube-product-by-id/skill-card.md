## Description: <br>
Submits Dataify Builder jobs that collect basic YouTube video information by video ID and returns the task ID and status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and submit Dataify YouTube video basic information collection tasks. It supports single or multiple video IDs, subtitle options, file naming, API TOKEN handling, and task status reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a Dataify API TOKEN from user input or the local environment. <br>
Mitigation: Review token use before running, avoid persisting the token unless future reuse is intended, and do not submit Builder jobs without an API TOKEN. <br>
Risk: Incorrect video IDs, subtitle options, selected-only values, or file names can create failed or unintended Dataify tasks. <br>
Mitigation: Review the parameter confirmation table and allowed option tables before confirming submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-product-by-id) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown parameter tables, shell commands, and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task_id, status, submitted parameters, shared settings, file name, dashboard URL, and a completion message after successful submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
