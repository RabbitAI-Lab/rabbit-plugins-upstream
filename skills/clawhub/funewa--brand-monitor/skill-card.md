## Description:

Helps Amazon sellers monitor multiple ASINs for review trends, negative-feedback spikes, competitor comparison, VOC reports, operational insights, alerts, and review/report exports through ARI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to track brand reputation across ASINs, analyze review sentiment and recurring topics, compare competitors, receive negative-review alerts, and generate concise reports or exports for operational decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI analyses or collection can consume credits automatically when account auto-confirm rules apply.

Mitigation: Use “only quote, do not execute” or set autoconfirm off before paid reports when strict per-action approval is required.

Risk: The skill sends Amazon ASIN, review, and account authorization data to ARI and stores an ARI API key locally.

Mitigation: Install only if ARI data handling is acceptable; avoid sharing API keys in chat and revoke or rotate keys from the ARI account page when needed.

Risk: Persistent confirmation settings can change how future paid actions are approved.

Mitigation: Review or reset autoconfirm settings before running paid workflows, especially on shared machines or accounts.

Risk: Interrupted paid commands may already have generated a report and charged credits.

Mitigation: Check the latest report for the ASIN before retrying a confirmed paid command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/brand-monitor)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [README](artifact/README.md)
- [Usage guide](artifact/使用说明.md)
- [ARI API reference](artifact/references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Conversational Markdown or text with optional local CLI commands and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; some analysis and collection actions may consume ARI credits according to account confirmation settings.]

## Skill Version(s):

1.4.13 (source: SKILL.md frontmatter, artifact/_meta.json, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
