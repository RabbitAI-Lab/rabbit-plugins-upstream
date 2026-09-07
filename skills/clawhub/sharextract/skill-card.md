## Description:

Extract normalized content from public share URLs, RSS/Atom feeds, timed-text/subtitle documents, and web pages using a protocol-first fallback ladder.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuaishare](https://clawhub.ai/user/wuaishare)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use ShareXtract to retrieve normalized content from already-public share links, feeds, captions, articles, and public metadata surfaces while preserving extraction method, confidence, warnings, and source boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote pages, captions, feed entries, comments, and metadata may contain prompt-injection text or misleading instructions.

Mitigation: Treat extracted payloads as untrusted data, preserve quotation and data boundaries, and require independent user intent before taking any downstream action.

Risk: Installing the external runtime, optional extras, browser support, MCP, or HTTP service modes expands the execution and network surface.

Mitigation: Install the runtime in a virtual environment or container, pin the intended release, and enable optional extras or service modes only when they are needed.

Risk: The skill could be misapplied to content behind login walls, CAPTCHAs, paywalls, WAF challenges, private links, or other access controls.

Mitigation: Use it only for content already public to the requester and stop instead of adding credentials, copied sessions, CAPTCHA solving, stealth, or access-control bypasses.

## Reference(s):

- [ShareXtract ClawHub listing](https://clawhub.ai/wuaishare/skills/sharextract)
- [Platform matrix and extraction policy](references/platform-matrix.md)
- [Adding an adapter](references/adding-adapters.md)
- [Ecosystem map](references/ecosystem.md)
- [Adapter health and fixture corpus](references/adapter-health.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and normalized JSON or Markdown extraction outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Extraction outputs may include source URL, canonical URL, platform, kind, extraction method, confidence, title, author, text, markdown, metadata, warnings, and retrieval time.]

## Skill Version(s):

0.23.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
