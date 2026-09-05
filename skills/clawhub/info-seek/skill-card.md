## Description:

Infoseek helps agents run multi-source research workflows that discover sources, score them, fetch content, analyze contradictions and entities, and produce structured Markdown reports with optional local archives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gyint](https://clawhub.ai/user/gyint)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agent builders use this skill to automate industry, market, policy, technology, competitor, company, or person research into sourced Markdown reports and optional local knowledge archives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist research state and archives locally and includes file-management behavior.

Mitigation: Run it in a controlled environment, set data and archive locations deliberately, and review file deletion or recycle behavior before enabling it.

Risk: The skill includes credential-management and external API capabilities.

Mitigation: Use least-privilege API keys, avoid broad default credentials, prefer OS keyring storage where appropriate, and disable credential tools that are not needed.

Risk: Remote server modes can expose research and tool operations over the network.

Mitigation: Use local stdio mode when possible; for remote SSE or hosted use, require strong bearer tokens and remove default OAuth client or secret values before deployment.

Risk: Identity-attribution and OSINT features can process personal public data.

Mitigation: Keep these capabilities disabled unless there is a lawful, authorized use case, require explicit consent, and audit any enabled use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gyint/skills/info-seek)
- [SKILL.md](SKILL.md)
- [README.md](README.md)
- [RELEASE_NOTES.md](RELEASE_NOTES.md)
- [Configuration Reference](references/configuration.md)
- [API Keys Reference](references/api-keys.md)
- [External Dependencies](references/external-deps.md)
- [Risk Register](references/risk-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON-like tool responses, Python snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source summaries, contradiction analysis, entity information, traced exports, and local archive paths.]

## Skill Version(s):

1.4.1 (source: frontmatter, package.json, CHANGELOG, released 2026-08-30)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
