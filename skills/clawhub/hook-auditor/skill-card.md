## Description: <br>
Hook Auditor audits Claude Code hook registrations, identifies which hooks are truly active, estimates token and latency cost, and guides cleanup after user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jianyangzhai](https://clawhub.ai/user/jianyangzhai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Claude Code users use this skill to inspect installed hooks, distinguish active hooks from cached hook files, understand recurring token or latency cost, and clean up unintended hook registrations only after confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Claude Code configuration under ~/.claude to inspect hook registrations. <br>
Mitigation: Run it only when you want a hook audit and are comfortable with the agent inspecting Claude Code hook configuration. <br>
Risk: Cleanup actions can alter persistent Claude Code behavior. <br>
Mitigation: Require explicit user confirmation, create backups before edits, and review proposed changes before applying them. <br>
Risk: Broad activation triggers may cause the skill to run during general complaints about speed, token use, or unexpected automation. <br>
Mitigation: Confirm the user's intent to audit hooks before running scans or proposing configuration changes. <br>


## Reference(s): <br>
- [Hook event semantics quick reference](references/hook-events.md) <br>
- [ClawHub skill page](https://clawhub.ai/jianyangzhai/skills/hook-auditor) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands and optional JSON scan output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose configuration changes, but cleanup is documented as requiring user confirmation and backups.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
