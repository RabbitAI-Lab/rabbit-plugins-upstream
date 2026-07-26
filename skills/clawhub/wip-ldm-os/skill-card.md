## Description: <br>
LDM OS installer and updater for installing, updating, or checking status of LDM OS, a shared infrastructure layer for AI agent identity, memory, tools, and collaboration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parkertoddbrooks](https://clawhub.ai/user/parkertoddbrooks) <br>

### License/Terms of Use: <br>
Dual License: MIT + AGPLv3 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to have an agent inspect local LDM OS state, explain available release tracks, run dry-run install or update flows, and perform installation only after consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill manages infrastructure rather than only prompting, including persistent agent hooks, MCP registration, global npm installation, cron/process-monitor behavior, broad local backups, and possible shell-profile credential export. <br>
Mitigation: Review the dry run before installation, run health checks after changes, and install only on machines where LDM OS should manage multiple AI harnesses and shared local memory. <br>
Risk: Persistent hooks and shared memory can change how local AI agents start, remember context, and access tools. <br>
Mitigation: Confirm the planned hook, MCP, and shared-workspace changes before approving installation or updates. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/parkertoddbrooks/skills/wip-ldm-os) <br>
- [LDM OS Homepage](https://github.com/wipcomputer/wip-ldm-os) <br>
- [LDM OS Install Document](https://wip.computer/install/wip-ldm-os.txt) <br>
- [Product Reference](references/PRODUCT.md) <br>
- [Commands Reference](references/COMMANDS.md) <br>
- [Interface Detection Reference](references/INTERFACES.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires git, npm, node, and Node.js 18+; install and update flows should use dry-run review before making changes.] <br>

## Skill Version(s): <br>
0.4.86 (source: SKILL.md metadata, package.json, target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
