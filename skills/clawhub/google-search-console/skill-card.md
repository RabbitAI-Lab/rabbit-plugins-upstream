## Description:

Google Search Console API integration with managed OAuth for querying search analytics, managing sitemaps, and monitoring site performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and SEO operators use this skill to access Google Search Console through Maton-managed OAuth, retrieve site and search analytics data, and perform confirmed sitemap management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure from long-lived API keys or elevated installation steps.

Mitigation: Prefer Maton OAuth, avoid sudo or elevated package-manager installs unless required by policy, and never print, persist, or pass credentials on command lines.

Risk: A request could affect the wrong Google Search Console account, property, or sitemap.

Mitigation: Confirm the target account, connection, resource identifier, payload, and intended effect before any write, and list or read current state first.

Risk: OAuth authorization may grant broader access than the current task needs.

Mitigation: Use least privilege when authorizing Google Search Console access and revoke unused connections promptly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-search-console)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Search Console API Reference](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- [Search Analytics Query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
- [Sitemaps API](https://developers.google.com/webmaster-tools/v1/sitemaps)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and API usage patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for connection creation or Search Console writes.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
