## Description: <br>
Manage Coder workspaces and AI coding agent tasks via CLI, including listing, creating, starting, stopping, deleting, SSH command execution, and monitoring tasks with Claude Code, Aider, or other agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[developmentcats](https://clawhub.ai/user/developmentcats) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw agents use this skill to manage Coder workspaces, run commands inside those workspaces, and create or monitor Coder Tasks for AI coding agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on CODER_SESSION_TOKEN, which is sensitive credential material. <br>
Mitigation: Keep the token private, avoid committing or sharing it, and prefer least-privilege or short-lived tokens where possible. <br>
Risk: Workspace or task deletion commands and broad remote commands can have destructive effects in Coder environments. <br>
Mitigation: Require explicit confirmation before deleting workspaces or tasks or running broad remote commands. <br>


## Reference(s): <br>
- [Coder Workspaces on ClawHub](https://clawhub.ai/developmentcats/skills/coder-workspaces) <br>
- [Coder Docs](https://coder.com/docs) <br>
- [Coder CLI](https://coder.com/docs/install/cli) <br>
- [Coder Tasks](https://coder.com/docs/ai-coder) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the coder CLI and CODER_URL and CODER_SESSION_TOKEN environment variables.] <br>

## Skill Version(s): <br>
1.5.5 (source: server release metadata and CHANGELOG, released 2026-02-06) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
