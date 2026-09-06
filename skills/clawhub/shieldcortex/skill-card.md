## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use ShieldCortex to add persistent local memory, semantic recall, knowledge graph support, and memory-write protection against prompt injection, credential leakage, and poisoning across supported agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Durable local memory and auto-memory features can retain prompts, assistant replies, decisions, preferences, or confidential context on disk.

Mitigation: Review auto-memory and proactive recall settings before enabling integrations, and periodically inspect or delete stored memories in ~/.shieldcortex.

Risk: Cloud sync, configured webhooks, and license activation can send selected metadata or memory content outside the local machine when enabled.

Mitigation: Keep cloud sync and webhooks disabled unless approved for the workspace, and review Cloud API key, license, and content-mode settings before use.

Risk: First-use embedding downloads and npx fallback paths can perform outbound package or model fetches.

Mitigation: Preinstall the ShieldCortex binary or configure binaryPath, pre-seed the embedding model cache, or set SHIELDCORTEX_SKIP_EMBEDDINGS=1 when network fetches are not allowed.

Risk: The OpenClaw hook self-heal path can write hook files and remove named stale legacy hook directories during gateway bootstrap.

Mitigation: Disable mutating self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the selfHeal configuration when automatic hook-file changes are not acceptable.

## Reference(s):

- [ShieldCortex ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex source repository](https://github.com/Drakon-Systems-Ltd/ShieldCortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for installing, configuring, using, and auditing local memory and security integrations.]

## Skill Version(s):

4.54.15 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
