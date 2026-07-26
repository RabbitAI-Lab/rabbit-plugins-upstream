## Description: <br>
OpenClaw Vault audits credential exposure, inventories secret files, flags stale credentials, and reports risky permission, history, git, config, log, Docker, and URL credential patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security engineers use this skill to inspect local agent workspaces for credential exposure, stale secrets, and risky storage patterns before deciding what to remediate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect sensitive files and report sensitive paths or masked credential matches. <br>
Mitigation: Run it only in a trusted environment and treat generated reports as sensitive. <br>
Risk: Some remediation commands can change permissions or move, restore, or overwrite files. <br>
Mitigation: Prefer audit, exposure, inventory, or status first; use fix-permissions, quarantine, unquarantine, and protect only when file changes are intended. <br>
Risk: The security review verdict is suspicious because local credential auditing is purpose-aligned but has filesystem access and mutation behavior. <br>
Mitigation: Review and scan the skill before deployment, then run it with an explicit workspace path and least necessary privileges. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/atlaspa/skills/openclaw-vault) <br>
- [Publisher profile](https://clawhub.ai/user/atlaspa) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance, configuration] <br>
**Output Format:** [Plain text console reports with exit codes; remediation commands may also create JSON metadata sidecars.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python 3 and no external dependencies; output can include sensitive paths and masked credential matches.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
