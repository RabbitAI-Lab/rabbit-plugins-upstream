## Description:

A Xiaohongshu track-analysis agent that helps brands structure public notes, creator pages, and comments into evidence-bounded category strategy recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qomob](https://clawhub.ai/user/qomob)

### License/Terms of Use:

MIT

## Use Case:

Brand, marketing, and strategy teams use this skill before entering a category, launching a product, or revising Xiaohongshu content strategy. It guides keyword grouping, multi-sort sampling, deduplication, creator interpretation, comment behavior analysis, and GO/NO-GO or conditional-GO recommendations with explicit evidence boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional collector and integration helpers may process public Xiaohongshu content and comments using user-provided accounts, tokens, or platform subscriptions.

Mitigation: Run these helpers only with an authorized account, keep collection limits tight, follow platform terms and privacy obligations, and do not commit configuration files containing API tokens.

Risk: Public-content sampling can overstate demand, miss private customer behavior, or confuse engagement with purchase intent.

Mitigation: Require sampling scope, collection time, keyword coverage, and evidence boundaries in the final analysis, and validate business decisions with the brand's own exposure, click, conversion, and refund data.

Risk: Commercialized or sponsored content can distort category signals in heavy-placement categories.

Mitigation: Label each note's commercialization level, discount high-commercialization signals, and anchor conclusions in natural content and real user comments.

Risk: Sorting and overlap observations can be misread as platform algorithm conclusions.

Mitigation: Use sorting and duplicate-overlap patterns only as analysis heuristics, not as reverse engineering of Xiaohongshu ranking behavior.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qomob/skills/xhs-track-analysis)
- [Methodology](references/methodology.md)
- [Data Sources](references/data-sources.md)
- [Table Template](references/table-template.md)
- [Case Study](references/case-study.md)
- [Supervised Collector README](scripts/collector/README.md)
- [Integration Skeleton README](scripts/integrations/README.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown analysis tables and recommendations, with optional CSV/Markdown source reports and shell commands for helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include sampling limits, evidence boundaries, commercial-content calibration, and a decision conclusion.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
