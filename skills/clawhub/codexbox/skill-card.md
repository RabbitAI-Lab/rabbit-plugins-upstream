## Description:

Install, configure, or run Codex through the codexbox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use codexbox to install and run Codex against a workspace, or to connect HTTP, OpenAI-compatible, MCP, Telegram, and scheduled workflows for coding and file-management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTTP and MCP modes can allow unauthenticated run execution and workspace file access when their tokens are unset.

Mitigation: Set separate API and MCP tokens, and bind services to loopback or place them behind an authenticating proxy.

Risk: The wrapper can access the selected workspace and mounted credentials, and the one-line installer executes a remote script.

Mitigation: Use a trusted, dedicated environment; inspect the installer and wrapper before running, and consider pinning the image by digest.

Risk: Telegram access and scheduled jobs can trigger coding or workspace tasks without an interactive user present.

Mitigation: Restrict allowed Telegram chats and enable cron jobs deliberately.

## Reference(s):

- [codexbox setup](references/setup.md)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/codexbox)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with shell commands, configuration examples, and code/workspace task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include executable commands and workspace file operations.]

## Skill Version(s):

0.7.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
