## Description: <br>
Manage Duplicati backups on the server using secure Bearer tokens. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robnew](https://clawhub.ai/user/robnew) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and administrators use this skill to let an agent check Duplicati server status, resolve backup jobs by name, start selected jobs, and retrieve recent error logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent receives authenticated access to a Duplicati server through a bearer token. <br>
Mitigation: Treat DUPLICATI_TOKEN as an admin secret, keep it out of repositories and logs, and restrict Duplicati access to trusted networks. <br>
Risk: Starting the wrong backup job could trigger unintended backup activity. <br>
Mitigation: List and match backup jobs before starting a job, and confirm the intended backup when the user refers to it by name. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robnew/skills/duplicati-skill) <br>
- [Publisher profile](https://clawhub.ai/user/robnew) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Duplicati REST API command guidance, status summaries, job-resolution guidance, and token-based configuration instructions.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
