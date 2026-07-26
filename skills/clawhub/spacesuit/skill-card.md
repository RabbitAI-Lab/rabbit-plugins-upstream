## Description: <br>
Openclaw Spacesuit is a framework scaffold for OpenClaw workspaces that installs session protocols, memory structure, git workflow conventions, safety rules, handoff patterns, heartbeat checks, and local workspace automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jontsai](https://clawhub.ai/user/jontsai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to bootstrap and maintain an OpenClaw workspace with durable memory, safety guidance, handoff conventions, and local scripts for workspace setup, upgrade previews, and operator indexing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables broad local memory and cross-session workspace behavior. <br>
Mitigation: Review AGENTS.md, TOOLS.md, SECURITY.md, and the installed workspace files before enabling the framework; narrow or disable broad search, heartbeat, memory commit, and broadcast rules in shared or sensitive environments. <br>
Risk: The operator sync utility reads local OpenClaw session transcripts and writes operator metadata to state/operators.json. <br>
Mitigation: Run sync-operators.sh with --dry-run first, keep state/operators.json private, and use explicit workspace/profile settings when multiple OpenClaw profiles exist. <br>
Risk: Install and upgrade scripts create or modify root workspace files. <br>
Mitigation: Preview upgrades with the diff or dry-run commands and review marker-delimited changes before applying them to an active workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jontsai/skills/spacesuit) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [OpenClaw Command Center](https://github.com/jontsai/openclaw-command-center) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and workspace file templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local setup, upgrade, diff, and operator-sync scripts that create or modify workspace files when run.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
