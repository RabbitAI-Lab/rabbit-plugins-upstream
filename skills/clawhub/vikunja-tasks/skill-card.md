## Description: <br>
Manage tasks and projects on a self-hosted Vikunja instance through REST API-backed shell commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickian](https://clawhub.ai/user/nickian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and self-hosted Vikunja users use this skill to list, create, complete, and inspect tasks and projects, including due, overdue, notification, and monitoring workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crafted task search or filter values can execute local Python code before contacting Vikunja. <br>
Mitigation: Patch URL-encoding to pass search and filter values as arguments or environment variables, and avoid untrusted search/filter input until patched. <br>
Risk: A misconfigured Vikunja URL or overprivileged API token can expose or modify task data. <br>
Mitigation: Set VIKUNJA_URL to the intended HTTPS server and use a limited, revocable Vikunja token. <br>
Risk: Task creation, completion, project creation, and recurring Telegram notifications can change or disclose task data. <br>
Mitigation: Confirm write actions before running them and enable cron or Telegram delivery only when recurring external notifications are intended. <br>


## Reference(s): <br>
- [Vikunja filter syntax](https://vikunja.io/docs/filters) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance and terminal-style text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses VIKUNJA_URL and VIKUNJA_TOKEN to call a configured self-hosted Vikunja REST API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
