## Description:

brand-monitor helps Amazon sellers monitor multiple ASINs, track review sentiment and negative-review spikes, compare competitors, and generate ARI-backed review analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this skill to monitor brand reputation across ASINs, identify negative-review trends and alerts, compare competitors, and generate review-backed VOC or operational guidance from ARI-collected data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through collection, analysis, leaderboard, or advisory workflows, and some account rules may allow small paid actions without a fresh per-action prompt.

Mitigation: Review billing behavior before installing, use only an ARI account intended for this workflow, and ask the agent to quote only or to require confirmation before every paid action when that is desired.

Risk: The skill can change monitoring and account workflow settings when asked.

Mitigation: Confirm monitoring cadence, account confirmation settings, and any recurring cost implications before allowing setting changes.

Risk: Review analysis depends on ARI-collected Amazon review samples and may not cover all reviews, variants, or time periods.

Mitigation: Treat reports as decision support, check the sample range and collection window, and validate important business decisions with additional data when coverage is limited.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/brand-monitor)
- [ARI CLI and API Reference](references/reference.md)
- [Usage Guide](使用说明.md)
- [Release Changelog](CHANGELOG.md)
- [ARI service](https://ari.funewa.com)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with optional CLI JSON and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and can use ARI credits for collection, analysis, leaderboard, and advisory workflows.]

## Skill Version(s):

1.4.11 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
