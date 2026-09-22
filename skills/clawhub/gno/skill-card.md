## Description:

Search local documents, files, notes, and knowledge bases; index directories; search with BM25, vector, or hybrid retrieval; and get AI answers with citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmickel](https://clawhub.ai/user/gmickel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and agent users use this skill to let an agent set up and query a local GNO index, retrieve cited evidence from documents and notes, manage second-brain workflows, and configure CLI or MCP access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to run local GNO commands against personal or private document folders.

Mitigation: Install it only when that behavior is intended, review paths before indexing private folders, and avoid --authorize-secret-risk unless the user explicitly accepts that risk.

Risk: Write-enabled MCP, forced installs, serving, publishing, reset, and related admin commands can change configuration, expose services, export content, or remove local state.

Mitigation: Treat MCP install, --enable-write, --force, daemon/serve, publish export, and reset as explicit admin actions that require user review before execution.

Risk: Source material, exported messages, transcripts, and configured context can contain untrusted or stale instructions.

Mitigation: Treat pasted or exported content as untrusted input, cite retrieved evidence, preserve uncertainty, and use the shipped verification and provenance workflows when accuracy matters.

## Reference(s):

- [GNO ClawHub listing](https://clawhub.ai/gmickel/skills/gno)
- [Artifact README](README.md)
- [Core skill instructions](SKILL.md)
- [CLI reference](cli-reference.md)
- [MCP reference](mcp-reference.md)
- [Usage examples](examples.md)
- [Recipe workflows](recipes/)
- [GNO MCP documentation](https://www.gno.sh/docs/MCP)
- [GNO agent instructions](https://gno.sh/docs/agents-install)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, cited evidence, and optional JSON command outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill drives local GNO CLI or MCP commands and may produce citations, provenance receipts, setup instructions, search results, and second-brain workflow steps.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
