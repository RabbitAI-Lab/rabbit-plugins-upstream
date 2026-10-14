## Description:

Install, configure, or run Codex through the codexbox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run Codex in a Docker-backed workspace, automate coding tasks, and configure optional HTTP, MCP, Telegram, and scheduled access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated HTTP or MCP access may allow remote agent runs and workspace file access, including deletion.

Mitigation: Set distinct API and MCP bearer tokens before enabling either service; bind to loopback or use an authenticated proxy, and restrict access to trusted callers.

Risk: Codex can modify or delete files in the mounted workspace, and authentication state persists across runs.

Mitigation: Mount only the intended workspace, safeguard Codex credentials, and review destructive actions before execution.

Risk: A remote installer or floating container image may change without prior review.

Mitigation: Inspect installation scripts and prefer inspected or pinned images over floating latest tags.

## Reference(s):

- [codexbox release on ClawHub](https://clawhub.ai/psyb0t/skills/codexbox)
- [codexbox setup guide](artifact/references/setup.md)
- [codexbox project homepage](https://github.com/psyb0t/docker-codexbox)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with code and shell examples; Codex responses may also be returned as text or JSON through configured services]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional HTTP, MCP, Telegram, and scheduled delivery]

## Skill Version(s):

0.7.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
