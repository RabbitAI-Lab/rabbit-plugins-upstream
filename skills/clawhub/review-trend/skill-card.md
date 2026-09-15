## Description:

Analyzes Amazon review volume, ratings, sentiment, complaint themes, and reputation shifts over time to help users detect review-trend changes and product-quality risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and analysts use this skill to review Amazon ASIN feedback, monitor rating and sentiment trends, identify complaint themes, generate VOC or operational reports, compare competitors, and decide when to collect or monitor more review data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may spend ARI credits when server-side auto-confirmation applies to small paid analyses.

Mitigation: Set auto-confirmation off before use, or explicitly say 'only quote, do not execute' when asking for pricing.

Risk: Local exports may overwrite files if written into broad or sensitive directories.

Mitigation: Use a dedicated export directory and avoid using the home directory or project root as an export target.

Risk: The skill requires access to an ARI account through an API key.

Mitigation: Use the browser authorization flow or a dedicated API key, and do not paste secrets into reports, prompts, or command examples.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/funewa/skills/review-trend)
- [README](README.md)
- [User Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise text responses with optional shell command examples, report links, CSV exports, and Markdown or HTML report exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses ARI service data; some analysis and collection workflows may consume ARI credits.]

## Skill Version(s):

1.4.11 (source: frontmatter, _meta.json, release evidence, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
