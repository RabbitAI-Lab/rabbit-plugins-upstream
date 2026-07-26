## Description: <br>
Network data loss prevention for agent workspaces that scans skills and files for outbound URLs, suspicious domains, data exfiltration endpoints, and network function calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security reviewers use this skill to inspect agent workspaces and skills for outbound network exposure before deployment or during security review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review classifies this release as suspicious because it is a local network-risk scanner with commands that can automatically modify code files or disable other skills. <br>
Mitigation: Start with scan, domains, or status commands; use protect, block, or quarantine only after backups are available and the target workspace has been narrowed. <br>
Risk: Automated blocking or quarantine can comment out code or rename skill folders in the selected workspace. <br>
Mitigation: Point --workspace at the smallest directory that needs inspection and review any changed files or renamed skill folders before relying on the result. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/atlaspa/skills/openclaw-egress) <br>
- [Publisher profile](https://clawhub.ai/user/atlaspa) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Command-line text reports with exit codes and optional JSON allowlist configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and supports darwin, linux, and win32 according to package metadata.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
