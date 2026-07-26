## Description: <br>
Submits Dataify Builder jobs to collect Facebook personal profile data by profile URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users or developers use this skill to submit one or more Facebook personal profile URLs to Dataify Builder and receive the resulting task_id and status so they can view results in Dataify. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Facebook profile URLs submitted through the skill are sent to Dataify for collection. <br>
Mitigation: Use the skill only for profiles you are allowed to collect and only when you intend to process those URLs through Dataify. <br>
Risk: DATAIFY_API_TOKEN authorizes actions on the user's Dataify account. <br>
Mitigation: Treat DATAIFY_API_TOKEN as a credential, provide it only when needed, and avoid persisting it unless the user explicitly chooses to save it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-facebook-profile-by-url) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with parameter tables, shell command examples, and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns task_id, status, submitted parameters, file name, dashboard URL, and message when the helper script is used.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
