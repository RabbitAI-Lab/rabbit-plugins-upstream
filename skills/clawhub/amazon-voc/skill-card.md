## Description:

Amazon Review Intelligence helps agents analyze collected Amazon reviews to surface pain points, purchase drivers, customer personas, trends, competitor differences, Listing and PPC keyword recommendations, monitoring alerts, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and analysts use this skill to turn ARI-authorized Amazon review data into VOC reports, competitor comparisons, review-monitoring summaries, keyword ideas, and operational recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid review collection or analysis can spend ARI credits automatically under server-side auto-confirm rules.

Mitigation: Use quote-only requests when estimating cost, keep autoconfirm off or set a low explicit limit, and require explicit confirmation when confirmationRequired is returned.

Risk: The ARI API key grants access to the user's ARI account.

Mitigation: Store keys only through local configuration or ARI_API_KEY, avoid including keys in reports or examples, and rotate keys after suspected exposure.

Risk: Retrying interrupted paid commands can duplicate spending if the server already generated and archived a report.

Mitigation: Check the latest reports or operation status before rerunning any confirmed paid command.

Risk: Reports are based on collected Amazon review samples and do not prove advertising results, inventory, orders, return rates, or complete review coverage.

Mitigation: State sample size and collection-window limits, and validate high-impact business decisions with additional operational data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/amazon-voc)
- [Server-Resolved Source Repository](https://github.com/funewa/Amazon-VOC)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [User Guide](artifact/使用说明.md)
- [ARI Web Product](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Natural-language summaries and Markdown reports, with optional JSON CLI responses and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ARI API authorization; paid actions may consume ARI credits and some reports include reportUrl links.]

## Skill Version(s):

1.4.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
