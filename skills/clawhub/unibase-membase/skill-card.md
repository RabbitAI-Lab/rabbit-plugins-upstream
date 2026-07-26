## Description: <br>
Manage agent memory with Membase - a decentralized, encrypted memory backup and restore system. Provides backup, restore, list, diff, status, and cleanup operations for agent memories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ibitnoah](https://clawhub.ai/user/ibitnoah) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw users and developers use this skill to back up, restore, list, compare, inspect, and clean up agent memory backups through Membase. It supports agent memory continuity workflows that need encrypted backup and restore operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Membase credentials and backup passwords, and its documentation includes commands that can print secrets or pass passwords through shell arguments. <br>
Mitigation: Do not echo secret environment variables, prefer protected environment or secret-manager injection, and avoid passing backup passwords directly on the command line. <br>
Risk: Restore operations can modify local agent memory files from a selected backup. <br>
Mitigation: Preserve current memory files before restore, verify the backup ID and source, and restore only when the user has explicitly confirmed the target backup. <br>
Risk: Status output can include configuration details in machine-readable JSON. <br>
Mitigation: Use --no-json for status output until configuration output is reviewed or redacted before sharing logs. <br>
Risk: The submitted artifact imports library modules that are not included in the artifact, limiting review of encryption, network, and restore behavior. <br>
Mitigation: Request and review a complete package that includes the lib implementation before relying on the skill for sensitive backups. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ibitnoah/skills/unibase-membase) <br>
- [Membase Documentation](https://github.com/unibaseio/membase) <br>
- [AgentSkills Specification](https://agentskills.io) <br>
- [OpenClaw Skills Guide](https://docs.openclaw.ai/tools/skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands operate on local memory files and Membase backups; many operations require Membase credentials and a backup password.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
