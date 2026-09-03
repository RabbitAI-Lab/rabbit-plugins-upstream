## Description:

This skill uses Amazon product details and review evidence to diagnose gaps in bullet-point selling points, customer questions, and wording, and it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operations teams use this skill to convert collected product and review evidence into bullet-point listing optimization guidance. It is scoped to listing bullet diagnostics and recommendations, not title rewriting, advertising automation, or automatic publishing to Amazon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can read or export Amazon product and review data.

Mitigation: Use a dedicated ARI key, do not include the key in prompts or reports, and review exported files and report links before sharing them.

Risk: The skill can initiate paid collection, analysis, monitoring, leaderboard, and workbench-advice actions.

Mitigation: Keep paid actions behind explicit user confirmation and consider setting ARI auto-confirm off before use when every paid action should be approved.

Risk: The released package is broader than the bullet-point optimization title suggests.

Mitigation: Review it as an Amazon review-operations assistant with collection, monitoring, competitor, export, and account-management behaviors before deployment.

Risk: Listing recommendations can be misleading when review samples are small, stale, or limited to a narrow collection window.

Mitigation: Surface sample size and analysis window in reports, treat small samples as directional, and validate recommendations against current product and business context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/bullet-writer)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [ARI CLI and API Reference](references/reference.md)
- [Amazon bullet optimization workflow](references/operation-workflow.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and concise natural-language guidance with optional shell command snippets and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN/site, sample size, analysis window, credits used, remaining balance, report IDs, and exported local files when the ARI service returns them.]

## Skill Version(s):

1.4.5 (source: server release evidence, skill frontmatter, _meta.json, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
