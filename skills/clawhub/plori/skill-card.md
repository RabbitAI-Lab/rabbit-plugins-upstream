## Description:

Runs background, parallel, and scheduled tasks on Plori cloud agents, saving results in persistent workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuchen-plori](https://clawhub.ai/user/yuchen-plori)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users delegate long-running builds, research, and scheduled automations to cloud workspaces, then retrieve the results and files after the chat ends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned remote installer commands can execute changing code on the user's machine.

Mitigation: Prefer MCP or manual installation; independently verify the installer before running pipe-to-shell commands or unpinned npx.

Risk: Persistent workspaces, schedules, and agents can keep running and spend credits after the chat ends.

Mitigation: Check credits and active runs and schedules, and stop or remove work that is no longer needed.

## Reference(s):

- [Plori skill release](https://clawhub.ai/yuchen-plori/skills/plori)
- [Plori MCP connection guide](https://plori.ai/mcp)
- [Plori CLI documentation](https://plori.ai/docs/cli)
- [Plori authentication guide](https://plori.ai/auth.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Text responses and saved workspace files; setup guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs can continue after the chat ends; retrieve saved files from the workspace.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
