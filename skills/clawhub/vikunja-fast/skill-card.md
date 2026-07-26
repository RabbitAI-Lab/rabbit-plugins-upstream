## Description: <br>
Manage Vikunja projects and tasks, including overdue and due-today views, task completion, and quick summaries via the Vikunja API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tmigone](https://clawhub.ai/user/tmigone) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and Vikunja users use this skill to inspect projects and tasks from an agent workflow, summarize due work, and mark selected tasks complete through the Vikunja API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses configured Vikunja API credentials and can access account task data. <br>
Mitigation: Install only for trusted Vikunja accounts, verify VIKUNJA_URL, prefer revocable or least-privileged tokens when available, and store credentials carefully. <br>
Risk: The done command changes task state for the selected task ID. <br>
Mitigation: Review task IDs before marking tasks complete and inspect task details with the show command when uncertain. <br>


## Reference(s): <br>
- [Vikunja](https://vikunja.io/) <br>
- [Vikunja Filters Documentation](https://vikunja.io/docs/filters/) <br>
- [Vikunja Fast on ClawHub](https://clawhub.ai/tmigone/skills/vikunja-fast) <br>
- [tmigone ClawHub Profile](https://clawhub.ai/user/tmigone) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and command output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses curl and jq against a configured Vikunja API URL with bearer-token or username/password authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
