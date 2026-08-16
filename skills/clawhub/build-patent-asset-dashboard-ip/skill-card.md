## Description:

Builds the patent-data layer for an applicant asset dashboard using PatSnap search and analytics APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

IP analysts and developers use this skill to retrieve applicant patent portfolios and build patent dashboard panels for patent-type subsets, filing trends, IPC/CPC classification distribution, filing-office coverage, top inventors, and innovation word clouds. It emphasizes documented collapse and counting rules for reproducible dashboard data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a PatSnap Open Platform API key.

Mitigation: Use a scoped key where possible, provide it through PATSNAP_API_KEY or a secure runtime argument, and avoid embedding or logging real credentials.

Risk: Some PatSnap global endpoints and entitlements may differ from the historical source environment.

Mitigation: Recheck endpoint availability in the authenticated PatSnap API catalog before execution and mark affected dashboard panels as data unavailable when an endpoint is not available.

Risk: Historical validation counts may be mistaken for current portfolio totals.

Mitigation: Treat source counts as regression provenance only and recompute current dashboard values from live PatSnap API responses.

## Reference(s):

- [PatSnap API Call Notes](references/api_notes.md)
- [PatSnap Authentication Guide](https://open.patsnap.com/devportal/guides/authentication)
- [P003 Analytics Query Search and Filter](https://open.patsnap.com/devportal/api-reference/patent-field/query)
- [P072 Classification Search Assistant](https://open.patsnap.com/devportal/api-reference/search/patent/classification/helper-search)
- [P066 Patent Classification Description](https://open.patsnap.com/devportal/api-reference/high-value-data/patent-classification-description)
- [A006 Top Inventors](https://open.patsnap.com/devportal/api-reference/insights/inventor-ranking)
- [A002 Innovation Word Cloud](https://open.patsnap.com/devportal/api-reference/insights/word-cloud-query)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request payloads and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PatSnap Open Platform API access; dashboard results depend on current endpoint availability and account entitlements.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
