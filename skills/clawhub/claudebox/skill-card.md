## Description: <br>
claudebox helps agents install, configure, launch, and script against a Dockerized Claude Code service exposed through CLI, HTTP, OpenAI-compatible, MCP, Telegram, and cron interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use claudebox to run Claude Code in a Docker container, expose it through automation-friendly interfaces, and manage installation, authentication, workspace, and server-mode configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthenticated API or MCP surfaces can expose prompt execution and workspace file operations. <br>
Mitigation: Set the per-mode bearer tokens before exposing ports, and bind services to loopback or an authenticating proxy when access should be limited. <br>
Risk: Mounting /var/run/docker.sock can grant host-level Docker control to the containerized service. <br>
Mitigation: Avoid mounting the Docker socket unless host Docker control is required, and use only on trusted hosts with limited workspaces and credentials. <br>
Risk: The default install path can run a downloaded shell script with the user's privileges. <br>
Mitigation: Download and inspect the installer before running it, or use the documented manual setup path. <br>
Risk: The service intentionally gives Claude Code broad shell, file, and optional network API access inside the container. <br>
Mitigation: Install only when that access is intended, and limit mounted workspaces, credentials, and exposed modes to the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/claudebox) <br>
- [Project homepage](https://github.com/psyb0t/docker-claudebox) <br>
- [claudebox setup](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown with shell, YAML, JSON, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary environment variable: CLAUDEBOX_URL; required binaries: docker and curl.] <br>

## Skill Version(s): <br>
2.3.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
