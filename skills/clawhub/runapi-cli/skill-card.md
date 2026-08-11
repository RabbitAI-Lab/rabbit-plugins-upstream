## Description:

Install and use the RunAPI CLI as the universal execution layer for RunAPI models. Use when the user asks to run any RunAPI model from an agent, inspect auth, install RunAPI on a local machine/server/CI, pass JSON request bodies, wait for tasks, or automate RunAPI workflows from the terminal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to install, authenticate, inspect, and run RunAPI model workflows from terminal, server, CI, or agent runtimes. It supports JSON-first model execution, task polling, pricing checks, file uploads, callback listener setup, and troubleshooting CLI or skill drift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing through a curl-to-sh command can execute remote installer code in the target environment.

Mitigation: Prefer the Homebrew install path when available; use the curl installer only where the RunAPI installer source is trusted.

Risk: API keys or listener secrets can be exposed through command arguments, logs, or committed configuration.

Mitigation: Use RUNAPI_API_KEY or stdin token import, keep credentials scoped, and do not commit webhook secrets or credentials.

Risk: Listener operations require browser-backed CLI credentials and may fail or select the wrong callback key if account state is not checked first.

Mitigation: Verify the active account and list API key metadata before listener use; pass an enabled callback API key ID explicitly when needed.

## Reference(s):

- [RunAPI model and CLI service catalog](https://runapi.ai/models.md)
- [RunAPI models homepage](https://runapi.ai/models)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-cli)
- [Publisher profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may reference RUNAPI_API_KEY, local config files, temporary file URLs, and command exit status handling.]

## Skill Version(s):

0.2.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
