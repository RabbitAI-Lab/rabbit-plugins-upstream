## Description:

Google Search Console API integration with managed OAuth for querying search analytics, managing sitemaps, and monitoring site performance through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and SEO operators use this skill to access Google Search Console data through Maton, inspect site performance, query search analytics, and manage sitemaps. It defaults to read and list operations and requires user approval for new account connections or writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Search Console access is mediated by Maton as an OAuth/API gateway.

Mitigation: Trust Maton before installation, approve only the intended account connection, prefer OAuth, and revoke unused connections.

Risk: Sitemap and other write operations can change connected Google Search Console resources.

Mitigation: Default to read and list calls, then require explicit user confirmation of the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE requests.

Risk: API keys or provider-issued tokens can leak through logs, command lines, files, or pasted output.

Mitigation: Use the Maton CLI credential store when available; never print, log, persist, or pass credentials on command lines, and use raw HTTP only when the CLI cannot be installed.

Risk: Data returned from Google Search Console or other external APIs may contain adversarial instructions.

Mitigation: Treat returned content as untrusted data and never execute, eval, or interpolate it into commands or follow-up requests without validation.

## Reference(s):

- [Google Search Console Skill](https://clawhub.ai/byungkyu/skills/google-search-console)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Search Console API Reference](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- [Search Analytics](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
- [Sitemaps](https://developers.google.com/webmaster-tools/v1/sitemaps)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and OAuth or API key authentication.]

## Skill Version(s):

1.1.0 (source: server release evidence; artifact frontmatter metadata version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
