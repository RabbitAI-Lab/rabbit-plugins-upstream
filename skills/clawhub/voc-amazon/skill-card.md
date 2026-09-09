## Description:

VOC洞察Amazon helps agents analyze Amazon review data through ARI to produce voice-of-customer reports covering pain points, purchase drivers, user personas, trends, competitor comparisons, and listing recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and Amazon sellers use this skill to turn ASIN review data into concise answers, VOC reports, competitor comparisons, keyword insights, monitoring summaries, and listing or product-improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits through review collection, VOC generation, analysis, leaderboard, and related workflows.

Mitigation: Use quote-only requests for pricing checks, keep auto-confirm disabled or bounded, and require clear user approval before confirmed paid operations.

Risk: Account auto-confirm settings can allow some paid workflows to execute before a fresh confirmation prompt.

Mitigation: Tell the agent to set auto-confirm off when fresh approval is required for every paid action, and review returned credit usage after each generated report.

Risk: Monitoring, competitor bindings, and watch management can change future data collection behavior and costs.

Mitigation: Review any request that creates, changes, resumes, pauses, or deletes monitoring or competitor relationships before execution.

Risk: The skill depends on a local ARI API key for account access.

Mitigation: Authorize through the browser flow or hidden local configuration, avoid pasting keys into chat, and revoke or rebuild keys from the ARI account page if compromised.

Risk: Export commands can write report or review files to local paths.

Mitigation: Use trusted export destinations and avoid arbitrary or sensitive filesystem paths.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/voc-amazon)
- [README](README.md)
- [Usage Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown and text summaries, CLI command guidance, configuration steps, and optional local CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may call paid ARI workflows when the user authorizes the action or account auto-confirm rules apply.]

## Skill Version(s):

1.4.8 (source: server release, SKILL.md frontmatter, CHANGELOG, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
