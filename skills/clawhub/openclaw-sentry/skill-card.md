## Description: <br>
Scans agent workspaces for leaked API keys, tokens, passwords, private keys, credentials, high-risk files, and missing secret-protection gitignore patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to check local workspaces for exposed secrets before continuing work, sharing files, or committing changes. It is most appropriate for local review workflows where the user wants fast secret-detection guidance without external dependencies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect sensitive workspace files while scanning for secrets. <br>
Mitigation: Run scan, check, or status with an explicit --workspace path and review results locally before taking further action. <br>
Risk: Some commands can rewrite files, move files into quarantine, or update repository metadata. <br>
Mitigation: Avoid redact, quarantine, defend, and protect unless the script has been reviewed and current backups exist. <br>


## Reference(s): <br>
- [Openclaw Sentry on ClawHub](https://clawhub.ai/atlaspa/skills/openclaw-sentry) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Analysis, Text] <br>
**Output Format:** [Markdown with inline bash code blocks and local scan result text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local secret-scan recommendations and command examples; scan commands return exit codes 0, 1, or 2 for clean, warning, or critical findings.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
