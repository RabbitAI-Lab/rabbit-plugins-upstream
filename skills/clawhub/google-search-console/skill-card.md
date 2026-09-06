## Description:

Google Search Console API integration through Maton-managed OAuth for querying search analytics, managing sitemaps, and monitoring site performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Google Search Console data through Maton, inspect search performance, list verified sites, and manage sitemaps with explicit approval for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Search Console actions are routed through Maton and require the user to trust that service with API access.

Mitigation: Install only when comfortable using Maton as the gateway, prefer OAuth, and grant the narrowest available Google Search Console scopes.

Risk: Sitemap changes or deletes can affect site indexing behavior.

Mitigation: Confirm the exact site URL, sitemap path, request payload, and intended effect before any PUT, POST, PATCH, or DELETE operation.

Risk: Using MATON_API_KEY exposes a long-lived credential more broadly than OAuth-backed CLI storage.

Mitigation: Use OAuth through the Maton CLI whenever possible and reserve MATON_API_KEY for environments where the CLI cannot be used.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-search-console)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Google Search Console API Reference](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- [Search Analytics](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
- [Sitemaps](https://developers.google.com/webmaster-tools/v1/sitemaps)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and optional Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should default to read/list Google Search Console calls and require explicit user approval for connection creation or write operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
