## Description:

Inkwell helps agents turn Markdown into WeChat-compatible HTML, generate magazine covers and social cards, and prepare content for clipboard or WeChat draft publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lijinhongucl-pixel](https://clawhub.ai/user/lijinhongucl-pixel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, and publishing agents use this skill when a user explicitly asks to format Markdown for WeChat, create cover or social-card assets, check content, or publish prepared article drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs a pinned external Python package.

Mitigation: Install in an isolated virtual environment, prefer the hash-checked requirements path, and verify the wheel hash against the supplied supply-chain notes before use.

Risk: Publishing or CDN workflows can send article content or images to GitHub, jsDelivr, WeChat, or the system clipboard.

Mitigation: Only provide GitHub or WeChat credentials when those transfers are intended, and obtain user confirmation before publish operations.

Risk: Markdown containing external image URLs can trigger outbound downloads during local preview generation.

Mitigation: Use --no-embed-external for sensitive, offline, internal-network, or untrusted Markdown.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/lijinhongucl-pixel/skills/inkwell-press)
- [Project homepage](https://github.com/lijinhongucl-pixel/inkwell)
- [Changelog](https://github.com/lijinhongucl-pixel/inkwell/blob/main/CHANGELOG.md)
- [Issues](https://github.com/lijinhongucl-pixel/inkwell/issues)
- [Supply chain audit notes](artifact/SUPPLY_CHAIN.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead the agent to create local HTML, cover, card, validation, clipboard, or WeChat draft outputs through the documented inkwell CLI.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
