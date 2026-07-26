## Description: <br>
Unified security suite for agent workspaces that installs, configures, scans, checks status, updates, and orchestrates 11 OpenClaw security tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security-minded agent workspace operators use this skill to install and coordinate OpenClaw security tools for integrity checks, secret scanning, permission review, network DLP, supply chain scanning, audit trails, compliance checks, and incident response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This skill can bulk-install or update 11 companion security tools in a workspace. <br>
Mitigation: Use an explicit workspace path, install only from a trusted publisher, and review installed companion tools before relying on setup, scan, update, or status results. <br>
Risk: Automated protection commands may make workspace changes such as quarantine, blocking, revocation, rotation, rollback, containment, or remediation. <br>
Mitigation: Run protect only after reviewing the workspace state and confirming that automated countermeasures are appropriate for the environment. <br>
Risk: The server security verdict is suspicious because the suite can execute and coordinate broad security actions without enough scoping or confirmation safeguards. <br>
Mitigation: Prefer read-only scan and status commands first, review command output, and avoid unpinned bulk updates in important workspaces. <br>


## Reference(s): <br>
- [OpenClaw Security on ClawHub](https://clawhub.ai/atlaspa/skills/openclaw-security) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) <br>
- [OpenClaw Warden](https://github.com/AtlasPA/openclaw-warden) <br>
- [OpenClaw Sentry](https://github.com/AtlasPA/openclaw-sentry) <br>
- [OpenClaw Arbiter](https://github.com/AtlasPA/openclaw-arbiter) <br>
- [OpenClaw Signet](https://github.com/AtlasPA/openclaw-signet) <br>
- [OpenClaw Ledger](https://github.com/AtlasPA/openclaw-ledger) <br>
- [OpenClaw Egress](https://github.com/AtlasPA/openclaw-egress) <br>
- [OpenClaw Sentinel](https://github.com/AtlasPA/openclaw-sentinel) <br>
- [OpenClaw Vault](https://github.com/AtlasPA/openclaw-vault) <br>
- [OpenClaw Bastion](https://github.com/AtlasPA/openclaw-bastion) <br>
- [OpenClaw Marshal](https://github.com/AtlasPA/openclaw-marshal) <br>
- [OpenClaw Triage](https://github.com/AtlasPA/openclaw-triage) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text] <br>
**Output Format:** [Markdown guidance with shell commands and command output text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.8+ and uses explicit workspace paths for command execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
