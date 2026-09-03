## Description:

Amazon-VOC helps agents collect Amazon reviews through ARI and produce VOC insight reports covering negative-review pain points, purchase drivers, user profiles, use cases, listing recommendations, competitor comparisons, and trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and their agents use this skill to collect review data, generate VOC and operations reports, compare competitors, monitor negative feedback, and turn customer language into product and Listing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits automatically under service-controlled auto-confirm rules.

Mitigation: Review or disable autoconfirm before use if every paid action should require explicit approval.

Risk: Schedules, competitor bindings, watch creation, and product-monitoring changes can persist beyond the current chat.

Mitigation: Confirm persistent monitoring changes before enabling them and periodically review ARI product, schedule, competitor, and watch settings.

Risk: The skill requires an ARI API key and can access account-scoped ARI data.

Mitigation: Use a dedicated ARI API key, store it only in supported local configuration or ARI_API_KEY, and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub Amazon-VOC Skill Page](https://clawhub.ai/funewa/skills/amazon-voc)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI API Service](https://ari.funewa.com)
- [ARI API Key Management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise text guidance, with optional CSV, Markdown, or HTML exports from ARI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses ARI credits for paid collection, analysis, leaderboard, advise, and monitoring workflows.]

## Skill Version(s):

1.4.5 (source: server release evidence, artifact frontmatter, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
