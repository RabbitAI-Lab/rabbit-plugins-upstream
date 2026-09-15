## Description:

Generates Amazon review insight reports that cover customer profiles, purchase drivers, use cases, pain points, unmet needs, competitor comparisons, trends, and product improvement opportunities with conclusions traceable to review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, product teams, and market researchers use this skill to analyze Amazon ASIN reviews, generate VOC and consumer insight reports, compare competitors, monitor negative review signals, and export review or report data for product and listing decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI authorization stores a local API key for the user account.

Mitigation: Use the documented browser authorization or configuration flow, never paste the key into reports or chat, and revoke or recreate the key from the ARI account page if needed.

Risk: Paid collection and report flows may spend ARI credits when account auto-confirm rules allow it.

Mitigation: Ask for quote-only behavior or require every paid action to ask first before running paid collection, report, leaderboard, or advice flows.

Risk: Monitoring, competitor, schedule, and workbench actions can change account state or ongoing review workflows.

Mitigation: Review the target ASIN, watch ID, schedule, competitor relationship, and stated cost before requesting a state-changing action.

Risk: Exports write review or report files locally.

Mitigation: Keep exports in the intended directory and review returned saved paths before sharing or relying on exported files.

Risk: Analysis is based on ARI-collected review samples and may not cover every Amazon review or variant.

Mitigation: Include the sample range and data limits in conclusions, and avoid trend or competitor claims when the sample size or time window is insufficient.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/consumer-insight)
- [README](artifact/README.md)
- [Usage guide](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Concise text summaries and Markdown reports, with optional CSV, Markdown, or HTML exports and links to online ARI reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ARI authorization and an ARI API key; analysis is based on ARI-collected Amazon review samples and may include credit usage, sample range, report IDs, report URLs, or local export paths.]

## Skill Version(s):

1.4.11 (source: frontmatter, _meta.json, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
