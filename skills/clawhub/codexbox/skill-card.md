## Description: <br>
codexbox runs OpenAI Codex CLI inside an aicodebox container and exposes it through shell, HTTP REST, OpenAI-compatible chat, MCP, Telegram, and cron workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to run Codex programmatically from scripts, CI, OpenAI-compatible clients, MCP-aware agents, Telegram, or scheduled cron jobs. It is also used to manage workspace files over HTTP when a terminal session is not the preferred interface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthenticated API or MCP surfaces can expose agent execution and workspace file access to anyone who can reach the service. <br>
Mitigation: Set separate strong bearer tokens for API and MCP modes, bind ports to localhost, or place the service behind an authenticating proxy before exposing it. <br>
Risk: Networked Codex runs can read, write, or delete files in the mounted workspace, and file deletion has no undo. <br>
Mitigation: Use isolated workspaces, avoid shared writable mounts unless access is tightly controlled, keep backups for important data, and confirm destructive file operations. <br>
Risk: The one-line installer executes a remote shell script if piped directly into bash. <br>
Mitigation: Download the installer, inspect it, and then run it only after verifying that the source and channel are trusted. <br>
Risk: Cron and Telegram modes create persistent or remote-triggered agent execution with access to mounted workspace data and Codex credentials. <br>
Mitigation: Restrict Telegram chats and users, review cron schedules before enabling them, and scope credentials and mounted directories to the smallest practical access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/codexbox) <br>
- [codexbox setup](references/setup.md) <br>
- [docker-codexbox repository](https://github.com/psyb0t/docker-codexbox) <br>
- [OpenAI Codex CLI](https://github.com/openai/codex) <br>
- [docker-aicodebox repository](https://github.com/psyb0t/docker-aicodebox) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with shell, JSON, YAML, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API request examples, deployment configuration, and operational safety guidance.] <br>

## Skill Version(s): <br>
0.5.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
