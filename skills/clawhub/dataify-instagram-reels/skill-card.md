## Description: <br>
Submit Dataify Instagram Reel Information Builder tasks for three Instagram Reel collection modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit Dataify Builder jobs that collect Instagram Reel information by detail URL, list/profile URL, or website/list URL, then return the resulting task ID and status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill submits Instagram URLs, filters, file names, and a Dataify account token to Dataify Builder. <br>
Mitigation: Use it only for authorized collection tasks and only with a Dataify token intended for this external service. <br>
Risk: Saving DATAIFY_API_TOKEN locally could expose account access if the local environment is shared or compromised. <br>
Mitigation: Ask for explicit user confirmation before saving the token and prefer per-run tokens when persistence is not needed. <br>
Risk: Default sample parameters can create unintended collection jobs if submitted without review. <br>
Mitigation: Confirm the collection mode, Instagram URL, count, dates, and file name before submitting a Builder request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-instagram-reels) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns Dataify task_id, status, submitted parameters, file name, dashboard URL, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.2.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
