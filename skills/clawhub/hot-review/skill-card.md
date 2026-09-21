## Description:

This skill helps Amazon sellers and ecommerce operators analyze collected Amazon review data to identify buyer pain points, purchase motivations, trends, competitor differences, and Listing improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and product researchers use this skill to analyze ASIN review samples, compare competitors, validate product opportunities, monitor review changes, and produce VOC-driven recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits automatically when server-side auto-confirm rules apply.

Mitigation: Before analysis, tell the agent "only quote, do not execute" or "ask before every credit deduction" if you want explicit approval before charges.

Risk: The skill can change future confirmation settings for paid actions.

Mitigation: Allow autoconfirm changes only after a clear user request, and review the resulting confirmation rule after it is changed.

Risk: The skill uses the user's ARI account context, including saved API key access, Amazon review data, exports, monitoring settings, and credit balance.

Mitigation: Install and run it only in an environment where the agent is allowed to access that ARI account and the associated Amazon review data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/hot-review)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing and plans](https://ari.funewa.com/zh/billing)
- [ARI online reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational text and Markdown reports, with CSV or HTML exports when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and ARI-collected Amazon review data; some collection, analysis, or leaderboard operations may spend ARI credits.]

## Skill Version(s):

1.4.13 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
