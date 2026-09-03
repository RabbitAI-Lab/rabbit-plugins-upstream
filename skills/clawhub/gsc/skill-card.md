## Description:

Read Google Search Console properties, Search Analytics, URL Inspection, and sitemaps for explicit GSC SEO performance, indexing, and freshness analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdrhyne](https://clawhub.ai/user/jdrhyne)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, site owners, and developers use this skill to authorize read-only Search Console access, query Search Analytics performance, inspect URLs, and review sitemap status for properties they can access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local OAuth client secrets and tokens can expose read-only Search Console access if copied, pasted, or stored with weak permissions.

Mitigation: Keep credential files private, use the documented local OAuth flow, require owner-only file permissions, and revoke the OAuth grant when access is no longer needed.

Risk: Python dependencies are declared with minimum versions instead of pinned versions.

Mitigation: Pin or lock dependency versions in managed environments before deployment.

Risk: Search Console returns top rows and bounded queries can be partial.

Mitigation: Check the returned pagination and provider-top-rows metadata before treating results as complete.

Risk: Search Console query text, page URLs, and inspection results may contain untrusted content.

Mitigation: Treat returned values as data for analysis, not as instructions for the agent.

## Reference(s):

- [Search Analytics query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
- [URL Inspection](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect)
- [Installed-app OAuth](https://developers.google.com/identity/protocols/oauth2/native-app)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash examples and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search Console query outputs are bounded and include pagination, freshness, partial-result, and provider-top-rows metadata.]

## Skill Version(s):

1.3.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
