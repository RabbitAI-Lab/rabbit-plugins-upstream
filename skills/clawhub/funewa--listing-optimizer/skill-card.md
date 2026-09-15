## Description:

Listing Optimizer helps agents analyze Amazon review data through ARI to identify buyer pain points, purchase motivations, trends, competitor signals, and review-backed recommendations for product titles, bullet points, A+ content, and operational follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, ecommerce teams, and agents use this skill to turn ARI-collected Amazon reviews into listing optimization guidance, VOC reports, keyword insights, trend summaries, competitor comparisons, alerts, and exportable review or report artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits automatically when account auto-confirm rules allow paid VOC or analysis actions.

Mitigation: Use quote-only flows when the user asks only for pricing, report cost and balance before confirmation-required actions, and honor requests to require confirmation before paid work.

Risk: The skill can change account or workflow state, including monitoring schedules, competitor bindings, auto-confirm settings, alerts, and workbench statuses.

Mitigation: Run state-changing commands only after explicit user intent, and restate the target ASIN, operation, cost impact, and expected effect before executing.

Risk: The skill requires an ARI API key and access to the ARI service.

Mitigation: Use browser authorization or local key configuration, never place secrets in chat or reports, and stop if endpoint or redirect validation fails.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/listing-optimizer)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI user guide](artifact/使用说明.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI report center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Natural-language text and Markdown reports, with JSON CLI responses and optional CSV, Markdown, or HTML exported files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and sends API requests only to https://ari.funewa.com.]

## Skill Version(s):

1.4.11 (source: frontmatter, _meta.json, server release evidence, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
