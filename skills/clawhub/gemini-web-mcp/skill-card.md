## Description:

Operate an installed Gemini Web MCP server safely by inspecting tool manifests, choosing narrow read-only workflows where possible, managing explicit history, notebook, account, scheduled-action, and media tasks, and verifying generated artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a Gemini Web MCP server with narrow tool profiles, read-only discovery first, explicit approval for private or destructive actions, and verification of generated media outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP workflows can expose private account inventory, chat metadata, or chat text.

Mitigation: Prefer read-only manifests, diagnostics, and metadata discovery first; read, export, or text-scan private chats only after explicit user intent.

Risk: Browser cookie extraction can materialize sensitive account-authentication material in a local cache.

Mitigation: Obtain explicit user approval, restrict file access, never log or share cookie values, and remove cached material when it is no longer needed.

Risk: Destructive workflows can delete chats, scheduled actions, Gems, test artifacts, or session state.

Mitigation: Require explicit confirmation, prefer dry runs when available, retain returned remote IDs, and verify deletion with fresh read-back before claiming success.

Risk: Generated media and long-running research results can be misreported if inferred from response prose or routing labels alone.

Mitigation: Verify saved files, MIME type, dimensions or duration, backend evidence, and operation state before summarizing completion or deliverables.

## Reference(s):

- [Gemini Web Tool Surface Reference](references/tool_surface.md)
- [Gemini Web MCP Homepage](https://github.com/Luckycat133/gemini-web-mcp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline tool names, configuration values, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes narrow MCP tool profiles, explicit user approval for sensitive actions, and verification before reporting remote or media outcomes.]

## Skill Version(s):

0.1.1 (source: server evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
