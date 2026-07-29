## Description: <br>
Popcorn CLI helps agents use the Popcorn command-line client to query available image and video generation models, submit asynchronous generation tasks, and check task status by session or task ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zeyiy](https://clawhub.ai/user/zeyiy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, automation operators, and agents use this skill to configure popcorn-cli, inspect tenant-available models, submit Popcorn image or video generation jobs, and poll for final task results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Popcorn API key is stored in ~/.popcorn-cli/config.json as a local secret. <br>
Mitigation: Restrict local file access, avoid shared or poorly isolated machines, and keep the config file out of repositories, backups, logs, screenshots, and public support channels. <br>
Risk: Prompts, generation parameters, business context, session IDs, task IDs, and result URLs may be sent to or returned from the Popcorn backend. <br>
Mitigation: Do not include passwords, keys, personal data, customer confidential data, or other sensitive material in prompts, task parameters, logs, issues, chat records, or build artifacts. <br>
Risk: Backend URL configuration can direct requests to an unintended service. <br>
Mitigation: Keep backend URL configuration pointed only at a trusted Popcorn endpoint before running model, submit, or task-list commands. <br>


## Reference(s): <br>
- [Popcorn CLI Installation Guide](https://mangaforge-qa-1255521909.cos.ap-shanghai.myqcloud.com/docs/popcorn-cli/popcorn-cli-installation-guide.html) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may return task IDs, session IDs, status values, result URLs, and error messages from the Popcorn backend.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
