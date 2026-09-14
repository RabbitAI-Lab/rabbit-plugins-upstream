## Description:

Cross-Border helps agents analyze Amazon reviews across eight marketplaces to compare customer pain points, localization needs, listing language, trends, competitors, alerts, and exportable reports through ARI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce operators use this skill to understand review themes, low-star causes, cross-market differences, localization opportunities, competitor gaps, and monitoring needs for ASINs. Agents can use it to guide ARI authorization, quote paid work, run approved review analysis workflows, and summarize evidence-backed recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits when paid analysis or collection workflows run.

Mitigation: Use quote-only mode when requested, report the credit cost and balance before confirmed paid work, and ask before every credit deduction when the user wants stricter control.

Risk: The skill requires ARI account authorization and communicates with ari.funewa.com.

Mitigation: Use browser-based authorization, do not request passwords or expose API keys, and stop if an endpoint or redirect is blocked.

Risk: Some workflows can persist beyond the current chat by enabling monitoring, adding competitors, changing auto-confirm settings, or updating workbench status.

Mitigation: Review those requests with the user and require clear intent before making persistent account or workflow changes.

Risk: Exports can write reports or review data to local directories.

Mitigation: Avoid shared or untrusted export directories and rely on the package's allowed export directory checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/cross-border)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing and plans](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational text and Markdown reports with inline shell commands, optional CSV/HTML/Markdown exports, and ARI report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish data directly returned by ARI from interpretation and recommendations; small samples and limited collection windows should be called out.]

## Skill Version(s):

1.4.11 (source: frontmatter, _meta.json, release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
