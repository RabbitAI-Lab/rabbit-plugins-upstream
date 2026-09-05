## Description:

Use when the user wants a weekly (or other short-period) operating report of site movement \u2014 what changed, what was verified, what to do next \u2014 from whatever evidence tier is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Site operators and SEO teams use this skill to produce short-period operating reports that summarize measured site movement, verified changes, and the next concrete actions from available crawl, analytics, search, or TrustGrowth evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact refers to a provider-selection reference that is not included in this release.

Mitigation: Confirm the missing provider-selection reference is intentional before installation and use already-configured connectors only.

Risk: Reports can be misleading if partial windows, unavailable data, or user-provided exports are treated as measured evidence.

Mitigation: Preserve the reporting contract's fact labels, complete-window rule, and not-measured notes in every generated report.

Risk: Connector use may expose credentials or access data beyond the user's own sites.

Mitigation: Use read-only connectors that are already configured, never print keys, and require owner review before publishing or irreversible actions.

## Reference(s):

- [Connectors and Categories](artifact/references/connectors.md)
- [Reporting Contract](artifact/references/reporting.md)
- [Groundcrew WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [Groundcrew ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls, shell commands]

**Output Format:** [Markdown report with evidence labels, verdict, metrics table, actions, and not-measured notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report facts are labeled as Measured, User-provided, or Estimated; deltas compare only like-for-like sources.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
