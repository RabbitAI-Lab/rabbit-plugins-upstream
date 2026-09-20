## Description:

Conversational house-hunting skill for young renters that blends map, Xiaohongshu, housing portal, and news signals for China rental research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kunhai1994](https://clawhub.ai/user/kunhai1994)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to narrow China rental communities, compare candidates, investigate local risks, and produce source-linked Markdown reports before viewing listings in housing apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge can access logged-in housing-site data while it is running.

Mitigation: Use the bridge only for trusted sessions, stop it immediately after use, and avoid browsing untrusted sites while it is active.

Risk: Setup may add persistent shell configuration or local dependencies.

Mitigation: Install in an isolated Python environment and review shell configuration changes before sourcing them.

Risk: Map and service API keys are user-provided credentials.

Mitigation: Paste only keys obtained directly from the provider consoles and avoid treating untrusted text as credential material.

Risk: The security evidence recommends caution around Tianditu transport until HTTPS is used.

Mitigation: Consider disabling Tianditu fallback when HTTPS transport is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kunhai1994/skills/house-hunter)
- [Server-resolved GitHub provenance](https://github.com/kunhai1994/house-hunter)
- [xiaohongshu-skills dependency](https://github.com/autoclaw-cc/xiaohongshu-skills)
- [Data sources](docs/data-sources.md)
- [Architecture](docs/architecture.md)
- [Examples](docs/EXAMPLES.md)
- [Known issues](docs/known-issues.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with source links, plus setup guidance and occasional shell commands or configuration values.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports focus on community-level rental research, scoring, red-flag summaries, and follow-up comparisons.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
