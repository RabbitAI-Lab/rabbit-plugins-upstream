## Description: <br>
CLI tool that audits Claude Code and OpenClaw config files for misconfigurations, token waste, security issues, and stale authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI operations teams use this skill to have an agent install and run a local CLI that audits Claude Code and OpenClaw configurations, reviews findings, and proposes or applies approved optimizations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool is meant to inspect sensitive local agent configuration, including OpenClaw and Claude Code files. <br>
Mitigation: Run it only where local configuration inspection is acceptable, and review findings before acting on them; evidence states audit, scan, and optimize do not transmit config data. <br>
Risk: Optional monitoring installs a daily cron job and sends summary counts and check names. <br>
Mitigation: Enable monitoring only when that reporting is acceptable, preview the payload when needed, and disable monitoring to remove the cron entry. <br>
Risk: Licensed fix/apply commands may change OpenClaw configuration. <br>
Mitigation: Use dry-run and plan flows first, apply only human-approved changes, and rely on the documented backup, verification, and rollback behavior. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/jarvis-drakon/skills/drakon-agent-optimizer) <br>
- [Agent Optimizer product page](https://drakonsystems.com/products/agent-optimizer) <br>
- [npm package](https://www.npmjs.com/package/@drakon-systems/agent-optimizer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command-output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands inspect local agent configuration; licensed fix/apply commands can modify OpenClaw config after user-approved planning.] <br>

## Skill Version(s): <br>
0.13.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
