## Description: <br>
Full workspace security suite: detect unauthorized modifications, scan for prompt injection patterns, and automatically respond with countermeasures - snapshot restore, skill quarantine, git rollback, and automated protection sweeps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent-workspace operators use this skill to establish local integrity baselines, scan workspace files for prompt-injection patterns, and run manual or automatic countermeasures such as snapshot restore, git rollback, and skill quarantine. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic protection can overwrite workspace files or disable skills without a review step. <br>
Mitigation: Run baseline, verify, scan, or full manually first, inspect findings, and enable protect only after confirming the baseline and false-positive behavior are acceptable. <br>
Risk: .integrity snapshots can contain sensitive local workspace content. <br>
Mitigation: Treat the .integrity directory as sensitive local data and avoid sharing, publishing, or committing snapshots unless they have been reviewed. <br>
Risk: Startup hooks or heartbeat integration can apply countermeasures repeatedly before a human review. <br>
Mitigation: Use manual commands during initial adoption and add automatic hooks only after testing on the intended workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/atlaspa/skills/openclaw-warden-pro) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) <br>
- [OpenClaw Warden free version reference](https://github.com/AtlasPA/openclaw-warden) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; CLI commands emit plain-text reports and status messages.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Countermeasure commands can write .integrity snapshots, restore workspace files, run git rollback for tracked files, and rename skill directories for quarantine.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
