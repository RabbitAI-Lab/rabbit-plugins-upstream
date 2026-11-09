## Description:

A shopping research assistant that grades product evidence, checks public quality and safety records, and compares value before offering a recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhashushu](https://clawhub.ai/user/zhashushu)

### License/Terms of Use:

MIT

## Use Case:

External shoppers use the skill to evaluate a product category or model. It gathers current public safety, quality, and user-feedback evidence, grades sources, and compares total cost to support a qualified recommendation.

### Deployment Geography for Use:

China, with emphasis on Chinese regulatory and retail sources

## Known Risks and Mitigations:

Risk: The installer version may not be pinned.

Mitigation: Review the installer source and version before installation; pin the version when possible.

Risk: Product comparisons may be affected by a reported warranty-cost calculation issue.

Mitigation: Treat those comparisons cautiously and review the affected calculation before relying on it.

Risk: The security scan was partial because some references could not be resolved.

Mitigation: Check unresolved references before treating the scan as covering every referenced item.

## Reference(s):

- [Source credibility and evidence grading guide](references/source-credibility.md)
- [CCTV News: AI-generated product misinformation report](https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=12967278106578155767)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Text]

**Output Format:** [Chinese-language Markdown report with evidence grades, links, and comparison tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses current lookup for time-sensitive claims and can include script-derived cost comparisons.]

## Skill Version(s):

1.0.6 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
