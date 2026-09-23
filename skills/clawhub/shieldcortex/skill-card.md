## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to give agents persistent local memory, semantic recall, knowledge-graph context, and security checks for prompt injection, credential leaks, and memory poisoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist conversation-derived memory and inspect agent or project configuration, including sensitive files such as environment files.

Mitigation: Install only when persistent agent memory and local scanning are intended; review captured memory regularly and disable auto-memory or broad keyword capture for sensitive work.

Risk: Some paths can fetch packages or models, including the OpenClaw npx fallback and first-use embedding model download.

Mitigation: Prefer a pinned local or global shieldcortex install or configured binary path, pre-seed the embedding model cache, or set SHIELDCORTEX_SKIP_EMBEDDINGS=1 when remote model fetches are not acceptable.

Risk: Cloud sync can transmit selected memory or audit metadata when explicitly enabled.

Mitigation: Keep Cloud sync disabled unless the user accepts that data flow; enable it only with a deliberate API key configuration and review the selected sync scope.

Risk: The bundled hook can perform self-heal writes to OpenClaw hook locations and remove stale legacy hook copies.

Mitigation: Disable self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the selfHeal configuration option when automatic hook maintenance is not desired.

## Reference(s):

- [ShieldCortex ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex Documentation](https://shieldcortex.ai/docs)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [shieldcortex npm Package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub Profile](https://github.com/Drakon-Systems-Ltd)
- [ShieldCortex Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local memory context, scan summaries, setup guidance, and security recommendations for supported agent environments.]

## Skill Version(s):

5.1.0 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
