## Description: <br>
Check the execution status of a Dataify scraper task by task ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to check whether a Dataify Builder scraping task is still processing, succeeded, or failed, and to retrieve the JSON result when the task succeeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A successful status check may automatically download and print the full task JSON result, which can contain sensitive or large scraped data. <br>
Mitigation: Use the skill only in environments where printing full Dataify task output is acceptable, and review task sensitivity before running status checks. <br>
Risk: The skill contacts Dataify using DATAIFY_API_TOKEN. <br>
Mitigation: Provide the token through the environment only, avoid pasting it into chat or command lines, and restrict use to accounts and task IDs the operator is authorized to access. <br>


## Reference(s): <br>
- [Dataify task status endpoint](https://scraperapi.dataify.com/task_status) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-task-status) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON response text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May print the full Dataify task JSON result after a successful status response; API tokens are read from DATAIFY_API_TOKEN and redacted from output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
