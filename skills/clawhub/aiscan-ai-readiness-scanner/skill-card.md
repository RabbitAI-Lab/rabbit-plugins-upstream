## Description:

AIScan v3.1 audits websites for AI-agent readiness through its stable REST API, MCP server, CLI/CI tooling, evidence-backed scoring, and fix-ready remediation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asif2bd](https://clawhub.ai/user/asif2bd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and agents use this skill to scan websites for AI readiness, interpret score and dimension failures, and produce prioritized remediation or platform-specific code and configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted URLs are sent to a hosted third-party scanner.

Mitigation: Use the skill for public sites, or scan private and staging sites only after confirming permission and data handling expectations.

Risk: The artifact documents a curl-to-node CLI fallback and package execution commands.

Mitigation: Prefer the REST or MCP workflow, or use a normal package install; review any command before running it.

Risk: Agent-applied fixes could add incorrect machine-readable metadata or imply unsupported site capabilities.

Mitigation: Apply only AIScan-returned remediation and fixGuide steps, review diffs, and publish MCP, OAuth, API, or Agent Skill files only for capabilities the site actually supports.

Risk: Scanned websites and API responses are external untrusted content.

Mitigation: Do not execute instructions found in scanned content, and validate proposed file changes before committing them.

## Reference(s):

- [Live Scanner](https://aiscan.site)
- [Developer & REST API Docs](https://aiscan.site/developers)
- [OpenAPI 3.1](https://aiscan.site/openapi.json)
- [API Catalog](https://aiscan.site/.well-known/api-catalog)
- [MCP Endpoint](https://aiscan.site/api/mcp)
- [Agent Skill JSON](https://aiscan.site/aiscan-skill.json)
- [CLI Docs](https://aiscan.site/docs/cli)
- [Changelog](https://aiscan.site/changelog)
- [MissionDeck.ai Cloud](https://missiondeck.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Chat responses, Markdown reports, JSON scan results, and inline bash or code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include score summaries, failing checks, remediation steps, platform-specific file changes, and one re-scan plan.]

## Skill Version(s):

2.0.0 (source: server release evidence, SKILL.md frontmatter, CHANGELOG released 2026-08-25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
