## Description: <br>
Download the JSON result for a completed Dataify scraper task by task ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to retrieve JSON output for completed Dataify scraper tasks when they have a task ID and a Dataify API token available in the environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends DATAIFY_API_TOKEN to Dataify's download endpoint to retrieve task results. <br>
Mitigation: Keep DATAIFY_API_TOKEN in the environment only, avoid placing it in chat or command arguments, and install the skill only when Dataify access is intended. <br>
Risk: Task result content comes from a provider response and may contain unexpected or sensitive JSON data. <br>
Mitigation: Review returned JSON before sharing it, and do not automatically retry failed downloads when the provider reports an error. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-task-result) <br>
- [Dataify download endpoint](https://scraperapi.dataify.com/download) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [JSON response text or concise provider error text, with shell commands shown in Markdown when needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Dataify task ID and DATAIFY_API_TOKEN in the environment; the script redacts the API token from output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
