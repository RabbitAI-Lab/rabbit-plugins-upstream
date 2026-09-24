## Description:

Google Search Console API integration with managed OAuth for querying search analytics, managing sitemaps, and monitoring site performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent access approved Google Search Console data, run site performance queries, manage sitemaps, and set up explicitly approved Maton automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the integration can grant access to Google Search Console account data.

Mitigation: Prefer OAuth, choose the narrowest available scopes, and confirm the exact connection before approving access.

Risk: Write operations, sitemap changes, hosted functions, triggers, destinations, and raw API-key fallback can create lasting account or data-flow effects.

Mitigation: Require explicit user confirmation before each write or automation step, prefer credential-store backed OAuth, and avoid raw API keys unless the CLI cannot be installed.

Risk: Automated destinations can continuously forward event data after setup.

Mitigation: Keep destinations on Maton-controlled endpoints unless the user names and approves a specific third-party host and understands what data will be sent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-search-console)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Search Console API Reference](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- [List Sites](https://developers.google.com/webmaster-tools/v1/sites/list)
- [Search Analytics](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
- [Sitemaps](https://developers.google.com/webmaster-tools/v1/sitemaps)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and approved Google Search Console authorization.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
