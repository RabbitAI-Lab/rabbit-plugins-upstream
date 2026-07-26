## Description: <br>
Generate a daily work report by automatically discovering git repositories the user worked on, collecting commit logs across all branches, and summarizing CodeBuddy Agent session overviews. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and CodeBuddy users use this skill to collect local Git activity and CodeBuddy session summaries for a selected date and generate a structured daily work report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The collector can scan broad local development directories and include activity from private or unrelated repositories. <br>
Mitigation: Configure narrower search paths and exclusion rules before use, then review the generated report before sharing or committing it. <br>
Risk: CodeBuddy session overview content may include sensitive project context or assistant interaction details. <br>
Mitigation: Disable or remove session-content collection if it is not needed, and redact sensitive details from generated reports. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/legionspace-hackathon/skills/codebuddy-daily-report) <br>
- [README](artifact/README.md) <br>
- [Configuration Reference](artifact/references/config.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown daily report generated from structured JSON collection output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report language follows the user's preference; collection requires Python 3.6+ and git CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
