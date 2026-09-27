## Description:

Helps agents use Google Search Console through Maton to analyze search performance, inspect URL indexing, and manage sitemaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Website owners, SEO teams, and developers use this skill to review search analytics and indexing status, and to list, submit, or remove sitemaps for their connected sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad OAuth access could expose more site data than a task requires.

Mitigation: Review scopes, prefer read-only access, and approve each new connection explicitly.

Risk: Sitemap changes or automated actions could affect a site without the intended approval.

Mitigation: Confirm each write, hosted function, and trigger separately before enabling it.

Risk: Persistent destinations could forward site or event data to third-party URLs.

Mitigation: Review each destination and avoid persistent forwarding unless its recipients, data, and duration are understood.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/google-search-console)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Google Search Console API reference](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- [Google Search Console URL inspection](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Code]

**Output Format:** [Markdown guidance with CLI examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected account's permissions and available Search Console data.]

## Skill Version(s):

1.2.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
