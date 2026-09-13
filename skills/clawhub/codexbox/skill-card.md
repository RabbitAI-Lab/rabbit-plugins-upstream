## Description:

codexbox packages OpenAI Codex CLI in an aicodebox container and exposes it through shell, one-shot exec, HTTP REST, an OpenAI-compatible chat endpoint, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run Codex programmatically over HTTP, MCP, Telegram, cron, or an OpenAI-compatible API instead of only through a local terminal. It is suited for scripted agent runs, workspace file operations, SDK integration, and remote or scheduled Codex workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network-exposed API or MCP modes can run Codex and access workspace files when mode tokens are unset.

Mitigation: Set strong independent API and MCP bearer tokens before enabling those modes, bind services to localhost, or place them behind trusted authentication.

Risk: Workspace file operations include deletion with no undo.

Mitigation: Mount only task-specific workspaces and delete files only after confirming they are intended targets.

Risk: The quick installer can execute a remote script through bash.

Mitigation: Download, inspect, and verify the installer or image before running it.

Risk: Cron, Telegram, MCP, and API modes can automate Codex runs or expose privileged surfaces on shared systems.

Mitigation: Enable only the surfaces needed for the deployment and avoid running them casually on shared or internet-reachable machines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/codexbox)
- [codexbox setup](references/setup.md)
- [codexbox repository](https://github.com/psyb0t/docker-codexbox)
- [OpenAI Codex CLI](https://github.com/openai/codex)
- [aicodebox](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON API responses, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include workspace file changes, streamed or polled run results, MCP tool responses, Telegram messages, and cron run logs depending on the enabled interface.]

## Skill Version(s):

0.6.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
