## Description:

Amazon-VOC helps an agent collect Amazon reviews through ARI and generate voice-of-customer reports covering review pain points, purchase drivers, user profiles, scenarios, trends, competitor comparisons, and Listing optimization suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to ask an agent for review mining and VOC analysis from ASINs. It supports concise summaries, trend checks, competitor comparisons, Listing improvement guidance, monitoring workflows, and exported reports based on ARI-collected review data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits by generating paid reports or analyses.

Mitigation: Use quote-only requests for price checks and disable auto-confirm when every paid action should require explicit approval.

Risk: The skill can change future auto-confirm or monitoring settings that may affect later costs.

Mitigation: Review requested monitoring or auto-confirm changes before approval and keep paid monitoring disabled unless the recurring cost is acceptable.

Risk: Reports and exports are based on ARI-collected Amazon review samples and may not cover every review or variant.

Mitigation: Treat outputs as decision support, check the reported sample range, and validate conclusions against additional data when coverage is limited.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [ARI Amazon Review Assistant Usage Guide](使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/amazon-voc)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise text responses, with shell commands or local export paths when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, report identifiers, sample ranges, credit usage, and local CSV/Markdown/HTML export outputs when returned by ARI.]

## Skill Version(s):

1.4.8 (source: server release evidence, skill frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
