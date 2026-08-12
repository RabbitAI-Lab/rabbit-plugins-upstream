## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to add persistent local memory, semantic recall, knowledge graph search, and security controls around memory writes, tool outputs, prompt injection, credential leaks, and poisoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically modify hook installation paths at startup.

Mitigation: Review the self-heal behavior before enabling it, or disable it with SHIELDCORTEX_SKIP_SELF_HEAL=1 or selfHeal:false.

Risk: The skill handles sensitive transcripts, agent configs, MCP settings, and .env files.

Mitigation: Review ~/.shieldcortex/ regularly, avoid use in projects with prompts or environment files that should not be retained locally, and disable auto-memory or proactive recall when needed.

Risk: Cloud sync can transmit selected memory content when explicitly enabled.

Mitigation: Keep cloud sync disabled unless needed, and enable it only after confirming the intended data handling and API key configuration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex Docs](https://shieldcortex.ai/docs)
- [npm Package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local memory recall, security scan results, and setup or configuration guidance.]

## Skill Version(s):

4.47.40 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
