## Description:

Competitor Review helps agents collect and compare Amazon ASIN review data through ARI, identify competitor strengths and weaknesses, and produce comparison reports and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and product operators use this skill to analyze Amazon review samples for their own products and competitors, compare recurring praise and complaints, and turn those findings into positioning, listing, monitoring, and product-improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid analysis or review collection can spend ARI account credits automatically when account auto-confirm rules apply.

Mitigation: Before paid use, ask for "only quote, do not execute" or "ask me before every credit charge," and verify the auto-confirm setting in the ARI account.

Risk: The skill requires ARI account access through an API key or browser authorization.

Mitigation: Use the documented ARI authorization flow, do not share API keys in chat, and revoke or rotate keys from the ARI account page if access is no longer needed.

Risk: Review insights depend on the comments ARI has collected and may not cover every Amazon review, variant, or time period.

Mitigation: Check the reported sample range and time window before acting on trends or competitor comparisons, and collect more data when the sample is too small.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-review)
- [README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text responses with inline shell commands and links; optional CSV, Markdown, or HTML files when exporting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid analysis or collection may consume account credits under ARI confirmation rules.]

## Skill Version(s):

1.4.11 (source: frontmatter, _meta.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
