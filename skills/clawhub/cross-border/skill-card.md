## Description:

Helps agents analyze Amazon review data across eight marketplaces to compare customer pain points, trends, competitors, and localization opportunities for cross-border e-commerce products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and their agents use this skill to turn collected Amazon review data into cross-market VOC summaries, trend checks, competitor comparisons, and localization or listing-improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some report-generation flows can consume credits automatically under the user's account auto-confirm rules.

Mitigation: Review the account confirmation setting before use, use quote-only checks when exploring costs, and turn auto-confirm off when every credit-consuming action should require approval.

Risk: The skill stores and uses a local ARI API key to access account and Amazon review-analysis data.

Mitigation: Use the documented browser authorization or environment-variable flow, avoid sharing the key in chats or reports, and revoke or recreate the key if it may have been exposed.

Risk: Custom ARI endpoint environment variables could send account data or API-key-backed requests away from the official ARI service.

Mitigation: Keep the official ARI endpoints unless using an HTTPS endpoint you control and have intentionally enabled the custom-base opt-in.

Risk: Review analysis is based on ARI-collected samples and may not cover every Amazon review, variant, or current market condition.

Mitigation: State sample size, site, and time window in user-facing results, treat small samples as directional, and validate important decisions with additional data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/cross-border)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [User Guide](artifact/使用说明.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Conversational text and Markdown reports with occasional shell commands, configuration steps, links, and JSON-backed status or report data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include the data range, sample limitations, credit usage when relevant, and links to generated ARI reports when returned by the service.]

## Skill Version(s):

1.4.8 (source: evidence.json release, _meta.json, SKILL.md frontmatter, and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
