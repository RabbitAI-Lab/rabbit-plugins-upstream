## Description: <br>
OpenClaw Warden verifies workspace file integrity and scans agent identity, memory, config, and skill files for prompt injection patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to establish baselines, verify workspace changes, and scan files that agents read at startup for prompt injection patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Countermeasure commands can overwrite workspace files or disable installed skills. <br>
Mitigation: Use verify, scan, full, and status for report-only checks first; run protect, restore, rollback, and quarantine only after reviewing target files and keeping backups. <br>
Risk: Baselining or accepting an unreviewed workspace can normalize unauthorized modifications. <br>
Mitigation: Review reported file changes and injection findings before running baseline or accept. <br>


## Reference(s): <br>
- [Openclaw Warden ClawHub listing](https://clawhub.ai/atlaspa/skills/openclaw-warden) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and plain-text scanner reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and runs locally without external dependencies.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
