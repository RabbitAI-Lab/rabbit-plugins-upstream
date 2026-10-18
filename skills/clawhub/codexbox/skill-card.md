## Description:

Install, configure, or run Codex through the codexbox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use codexbox to run Codex in a Docker-backed workspace and, when needed, connect it to scripts, agent clients, Telegram, or scheduled tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Dockerized service can access the selected workspace and persisted Codex and SSH state.

Mitigation: Review workspace mounts and persisted state before installation; use a dedicated workspace when possible.

Risk: Exposed REST or MCP services may allow unauthenticated runs and workspace file access if their separate tokens are unset.

Mitigation: Set distinct strong REST and MCP bearer tokens before binding ports; keep services on loopback or behind an authenticating proxy.

Risk: File operations can delete workspace files without an undo path.

Mitigation: Confirm deletion targets and avoid shared workspaces for delete-capable file APIs.

Risk: Telegram and cron modes can start work without a person reviewing each run.

Mitigation: Enable unattended modes only for tasks and workspaces approved for autonomous execution.

Risk: Remote installation scripts and mutable container images can change between uses.

Mitigation: Inspect the installer before running it and pin or review the image where possible.

## Reference(s):

- [ClawHub codexbox release](https://clawhub.ai/psyb0t/skills/codexbox)
- [codexbox setup](references/setup.md)
- [codexbox project](https://github.com/psyb0t/docker-codexbox)
- [aicodebox project](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide interactive work or produce responses through HTTP, MCP, Telegram, and cron integrations.]

## Skill Version(s):

0.7.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
