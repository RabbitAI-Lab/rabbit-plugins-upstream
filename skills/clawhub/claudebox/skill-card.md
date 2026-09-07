## Description:

claudebox helps agents install, configure, launch, and script against Claude Code running inside a Docker container through CLI, HTTP, OpenAI-compatible, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run Claude Code in a containerized environment and expose it through CLI, HTTP, OpenAI-compatible, MCP, Telegram, or scheduled cron workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network-exposed agent surfaces can be unauthenticated when API or MCP bearer tokens are unset.

Mitigation: Set per-mode bearer tokens and bind services to localhost or place them behind a trusted authenticating proxy before exposing them.

Risk: Mounting /var/run/docker.sock can grant host-level container control to the agent or to an attacker who reaches an exposed service.

Mitigation: Avoid mounting the Docker socket unless the host is disposable or explicitly trusted and the workload requires it.

Risk: The documented installer path can execute a downloaded shell script with local user privileges.

Mitigation: Download, inspect, pin, and verify installers, images, and packages before running them.

Risk: Mounted SSH or deploy keys can broaden the impact of misuse or compromise.

Mitigation: Use narrowly scoped SSH and deploy keys and avoid sharing containers or mounted credentials with untrusted users.

## Reference(s):

- [claudebox setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/claudebox)
- [Project homepage](https://github.com/psyb0t/docker-claudebox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, configuration examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands and configuration that launch network-accessible agent services; review before execution.]

## Skill Version(s):

2.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
