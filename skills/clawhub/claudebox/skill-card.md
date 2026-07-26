## Description: <br>
claudebox helps agents install, configure, launch, and script against Claude Code running in a Docker container through CLI, HTTP API, OpenAI-compatible, MCP, Telegram, and cron interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use claudebox to run Claude Code in a container, expose it through selected automation surfaces, and integrate it with scripts, CI, MCP clients, OpenAI-compatible clients, Telegram, or scheduled jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthenticated server modes can expose agent execution and workspace file access when mode-specific tokens are unset. <br>
Mitigation: Set API and MCP bearer tokens before enabling network-facing modes, and bind services to localhost or place them behind a protected proxy. <br>
Risk: Mounting /var/run/docker.sock can grant host-level container control to the running agent or to an attacker who reaches the service. <br>
Mitigation: Avoid mounting the Docker socket unless the workload requires it, and use the deployment only on hosts you trust. <br>
Risk: Mounted workspaces and credentials are accessible to the containerized agent by design. <br>
Mitigation: Use scoped credentials, limit mounted directories to the task, and treat the container as a powerful coding environment rather than a boundary for untrusted input. <br>
Risk: Downloaded install scripts run with the user's privileges. <br>
Mitigation: Download and inspect install scripts before executing them instead of piping network content directly into a shell. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/claudebox) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [setup.md](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/docker-claudebox) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell, JSON, YAML, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance covers local CLI use, container setup, REST and OpenAI-compatible APIs, MCP configuration, Telegram mode, and cron scheduling.] <br>

## Skill Version(s): <br>
2.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
