## Description:

Helps agents query Google Search Console performance, inspect URL indexing, and manage sitemaps through a Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners, marketers, and developers use this skill to review search performance, check indexing status, and manage sitemaps for their connected properties. With separate approval, they can automate checks using hosted functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton mediates access to connected Google Search Console properties and their data.

Mitigation: Use the CLI/OAuth path when possible, connect only needed accounts and scopes, and install only if you trust Maton with that access.

Risk: Sitemap changes and other write actions can modify connected properties.

Mitigation: Start with read-only calls and confirm the target and effect with the user before each write.

Risk: Hosted functions, triggers, and destinations can run actions automatically or forward data outside Maton.

Mitigation: Review functions and triggers before approval, and separately confirm any destination that forwards data externally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/google-search-console)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Google Search Console API reference](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- [URL Inspection API](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with optional shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize search analytics, index status, and sitemap information returned for connected properties.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
