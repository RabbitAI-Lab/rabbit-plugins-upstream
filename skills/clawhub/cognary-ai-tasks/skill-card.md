## Description: <br>
Cognary Tasks helps agents manage Cognary task lists through cognary-cli, including listing, adding, updating, completing, reactivating, and deleting tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dboyne](https://clawhub.ai/user/dboyne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate their Cognary task list from natural task-management requests while preserving parseable CLI output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Cognary API key grants access to task-management operations. <br>
Mitigation: Use a dedicated or revocable Cognary API key when possible and avoid exposing it in prompts, logs, or shared files. <br>
Risk: Update and delete commands can modify or remove user tasks. <br>
Mitigation: Show the exact task title and ID before updating or deleting a task. <br>
Risk: Installing an unintended CLI package could run untrusted tooling. <br>
Mitigation: Confirm that cognary-cli is the intended package before installation. <br>


## Reference(s): <br>
- [Cognary Tasks on ClawHub](https://clawhub.ai/dboyne/skills/cognary-ai-tasks) <br>
- [Cognary Tasks App](https://tasks.cognary.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and readable task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses JSON CLI output for task operations and requires COGNARY_API_KEY for authenticated Cognary requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
