## Description: <br>
Openclaw Bastion helps agents scan workspace and runtime content for prompt injection patterns, hidden instructions, boundary risks, and command policy issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to inspect files, directories, and workspace boundaries for prompt injection indicators before an agent relies on that content. It is also useful for reviewing command allowlists and workspace posture during local agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ClawHub security evidence flags this release as suspicious because it includes commands that can rewrite, move, and persistently modify workspace and agent instruction files. <br>
Mitigation: Start with scan, check, boundaries, allowlist, or status commands; use protect, sanitize, quarantine, unquarantine, canary, or enforce only after reviewing affected files and backups. <br>
Risk: Active defense commands can change local files or create persistent policy, hook, quarantine, and canary artifacts. <br>
Mitigation: Run in a controlled workspace, keep version control or backups available, and inspect generated or modified files before relying on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/atlaspa/skills/openclaw-bastion) <br>
- [OpenClaw Project](https://github.com/openclaw/openclaw) <br>
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Terminal text reports, Markdown guidance, and JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with python3; some commands can create backups, policy files, hook configuration, quarantine files, and canary metadata.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
