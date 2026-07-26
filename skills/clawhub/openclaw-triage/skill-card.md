## Description: <br>
Incident response and forensics for agent workspaces, including investigation, event timelines, blast-radius assessment, and forensic evidence collection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atlaspa](https://clawhub.ai/user/atlaspa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, security responders, and agent-workspace maintainers use this skill to investigate suspicious workspace activity, correlate OpenClaw security-tool data, estimate scope, and preserve forensic evidence before remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan classifies the release as suspicious because some commands can change a workspace or invoke workspace-local helper tools. <br>
Mitigation: Install only when an active incident-response tool is intended; review the skill and prefer read-only investigation, timeline, scope, and evidence commands before workspace-changing actions. <br>
Risk: Containment, remediation, and protection workflows can move, copy, restore, or otherwise modify workspace files. <br>
Mitigation: Back up the workspace and preserve forensic evidence before running contain, remediate, or protect commands. <br>
Risk: Remediation may run local OpenClaw helper tools from the target workspace. <br>
Mitigation: Verify local OpenClaw helper tools and their paths before allowing remediation to execute them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/atlaspa/skills/openclaw-triage) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local text or JSON incident-response outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python 3 and no external dependencies; commands inspect workspace state and can write triage state, evidence snapshots, reports, backups, or quarantine data.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
