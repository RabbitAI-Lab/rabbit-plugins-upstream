## Description:

This skill helps Amazon sellers validate new product ideas before launch by using comparable product reviews to identify buyer complaints, willingness-to-pay signals, overused selling points, differentiation opportunities, and evidence-backed launch decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and product teams use this skill to evaluate whether a new product is worth launching and how to differentiate it using ARI-collected review evidence, competitor comparisons, trend signals, and listing improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through review collection and analysis workflows.

Mitigation: Use pricing-only requests such as "只报价，不执行" or configure auto-confirm to always ask before credit-consuming actions.

Risk: The skill requires connecting an ARI account and storing an API key locally.

Mitigation: Authorize only through the browser flow or environment variable intended for ARI, never paste the API key into chat or reports, and revoke or rotate the key if exposure is suspected.

Risk: The skill can change monitoring or account-related state, including review collection schedules and confirmation preferences.

Mitigation: Require explicit user intent before enabling monitoring, changing schedules, or updating auto-confirm settings, and report the cost or state change after execution.

Risk: Analysis is based on ARI-collected Amazon review samples and may not cover all reviews, variants, or time windows.

Mitigation: State the sample size, site, collection window, and known coverage limits in outputs, and avoid presenting unsupported trends or variant-level conclusions as facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/new-product)
- [README](README.md)
- [Usage guide](使用说明.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain-text agent responses with optional shell command snippets, ARI report links, and export guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include data scope, sample limitations, credit usage, current balance, report identifiers, and CSV, Markdown, or HTML export instructions when available.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
