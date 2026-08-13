## Description:

Provides Reddit ads competitive intelligence, category benchmarks, campaign audit guidance, creative ideas, and weekly ad intelligence briefs for paid social teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, growth teams, and performance marketing agencies use this skill to analyze Reddit ad competitors, compare campaign metrics against category benchmarks, audit exported Reddit Ads performance data, and draft human-reviewed creative and optimization recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may share aggregated Reddit Ads exports, competitor names, or campaign performance details with the skill.

Mitigation: Use aggregated, non-PII CSV exports where possible, redact unnecessary client identifiers, and handle campaign data under the user's internal data-handling rules.

Risk: Benchmark, spend, and performance estimates may be inaccurate or unsuitable for a specific advertiser.

Mitigation: Require confidence ranges, sample sizes, and sampling periods in outputs, and validate recommendations with controlled A/B tests before changing material budget allocations.

Risk: Third-party data-source access and Reddit platform-policy assumptions may vary by user, region, or account type.

Mitigation: Verify permitted data sources, Reddit terms, third-party API rights, and legal assumptions for the user's own use case before relying on competitive intelligence outputs.

Risk: Generated recommendations could be mistaken for automatic ad operations.

Mitigation: Keep outputs as recommendations, drafts, and checklists only; require a qualified human to review and publish any ad, bid, targeting, or account change.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heroinyan-stack/skills/redditads-intelligence)
- [Publisher Profile](https://clawhub.ai/user/heroinyan-stack)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Structured Markdown reports with tables, checklists, confidence ranges, and campaign recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should label spend estimates with confidence ranges, cite sample sizes for benchmarks, and keep ad-launch decisions under human review.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
