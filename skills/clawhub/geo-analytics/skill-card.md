## Description:

This skill helps agents retrieve read-only Vtag GEO analytics for site traffic, AI-engine answer sampling, brand visibility, cited pages, conversions, realtime activity, and invalid-traffic review after user-authorized access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gt-oliver](https://clawhub.ai/user/gt-oliver)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer customer-facing GEO analytics questions about how a website appears in AI-engine responses and how authorized site analytics report traffic, engagement, pages, conversions, and data-quality signals. It is suited for read-only analysis where the agent must preserve source attribution boundaries and avoid unsupported causal claims between AI citations and site visits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose non-public site analytics, realtime behavior, session details, and AI probe responses after authorization.

Mitigation: Only use it with authorized sites, avoid sharing raw sensitive analytics outside approved contexts, and summarize data when detailed records are unnecessary.

Risk: The optional shell helper stores a long-lived read-only access token locally.

Mitigation: Keep the token private with restricted local permissions or a credential store, and revoke it in the Vtag console when access is no longer needed.

Risk: Analytics results can be misleading if the agent infers causality between AI-engine citations and measured site visits or treats unmeasurable sources as zero.

Mitigation: Report engine-side sampling and site-side analytics separately, preserve the unknown-source bucket, and use the documented server metrics rather than recalculating from raw probe records.

## Reference(s):

- [Endpoint Reference](references/endpoints.md)
- [Metrics and Measurement Rules](references/metrics.md)
- [ClawHub Skill Page](https://clawhub.ai/gt-oliver/skills/geo-analytics)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and API-response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are read-only and depend on OAuth device authorization for one selected site.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
