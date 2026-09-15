## Description:

Analyzes Amazon review data across variants such as color, size, and specification to identify low-performing variants, stronger variants, recurring customer pain points, trends, and evidence-backed product or listing improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to analyze Amazon ASIN review samples, compare variant and competitor performance, and produce guidance for inventory, listing, and product improvement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and calls ari.funewa.com on the user's behalf.

Mitigation: Install only when comfortable delegating ARI account actions, keep API keys out of chat and reports, and revoke or recreate keys if exposure is suspected.

Risk: Some ARI flows can spend credits or change account behavior without a fresh approval in all cases.

Mitigation: Before use, configure ARI to ask before each paid action unless automatic spending is intended, and use quote-only flows when evaluating cost.

Risk: Export behavior can write local review or report files.

Mitigation: Export only to a dedicated, non-sensitive directory and avoid existing project, configuration, or credential-related files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/variant-analysis)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Usage Guide](artifact/使用说明.md)
- [ARI Account and API Key Management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Natural-language analysis and guidance, Markdown reports, CLI JSON responses, and optional CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some ARI analysis or collection flows can spend account credits, and export flows can write local files.]

## Skill Version(s):

1.4.11 (source: evidence.release.version, SKILL.md frontmatter, _meta.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
