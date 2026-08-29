## Description:

Use TokST to retrieve, store, govern, and hand off durable context across cloud workspaces or Local SQLite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthemty](https://clawhub.ai/user/anthemty)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect agents with TokST memory so they can retrieve prior context, record confirmed decisions, manage sessions, and hand off durable project knowledge across cloud workspaces or a local SQLite profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The remote installer can execute downloaded setup code on the user's machine.

Mitigation: Install only when TokST is trusted, inspect installer sources where required by policy, and prefer controlled installation paths for managed environments.

Risk: Observed Session Relay can expose sensitive workflow context if enabled during private work.

Mitigation: Use local mode for private material, pause relay during sensitive work, and prefer review-first relay settings before automatic memory compilation.

Risk: API keys or credentials could be captured if placed in chat, source control, URLs, or unprotected configuration.

Mitigation: Store keys only in protected client settings or environment variables and revoke unused keys from TokST dashboard controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anthemty/skills/tokst-memory)
- [TokST documentation](https://tokst.com/docs)
- [TokST help](https://tokst.com/help)
- [TokST MCP documentation](https://tokst.com/docs/mcp)
- [TokST Sessions documentation](https://tokst.com/docs/sessions)
- [TokST Local documentation](https://tokst.com/docs/local)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing commands generally request JSON output for machine-readable TokST responses.]

## Skill Version(s):

0.8.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
