## Description:

Helps agents run background, parallel, and scheduled tasks in Plori cloud workspaces and retrieve their results and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuchen-plori](https://clawhub.ai/user/yuchen-plori)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users delegate longer-running builds, research, and automations to Plori cloud agents, then review their results and saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication may expose a one-time OAuth callback URL if the browser fallback is used.

Mitigation: Prefer MCP or browser authentication; share a callback URL in chat only when the documented fallback is necessary.

Risk: Optional pipe-to-shell or unpinned CLI installation can execute unverified code.

Mitigation: Use pinned or verified CLI installation methods instead.

## Reference(s):

- [ClawHub plori release](https://clawhub.ai/yuchen-plori/skills/plori)
- [Plori MCP connection guide](https://plori.ai/mcp)
- [Plori authentication guide](https://plori.ai/auth.md)
- [Plori CLI documentation](https://plori.ai/docs/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses and saved workspace files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-running tasks may return progress before final results; saved files should be checked before use.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
