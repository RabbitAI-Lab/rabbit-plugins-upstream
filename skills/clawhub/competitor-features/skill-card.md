## Description:

Builds static feature-comparison matrices for a primary Amazon ASIN and authorized competitors from product fields and review evidence, flagging evidence gaps and experience differences without inferring sales, inventory, ads, orders, or true return rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and ecommerce analysts use this skill to compare a main ASIN with authorized competitor ASINs, identify feature gaps, and summarize review-backed differences for listing and product decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated ARI actions can consume credits under account confirmation or autoconfirm rules.

Mitigation: Keep autoconfirm set to ask every time for agent use, run free profile or quote steps first, and require explicit user confirmation when confirmationRequired is returned.

Risk: A local ARI API key is required, and custom ARI_BASE_URL settings could redirect authenticated requests.

Mitigation: Use the official ARI endpoint, avoid custom ARI_BASE_URL values unless intentionally configured, and never include API keys in reports or command examples.

Risk: Persistent monitoring or confirmation-setting changes can affect future collection behavior and costs.

Mitigation: Only change monitoring schedules or autoconfirm settings after an explicit user request, and restate the cost or current confirmation rule after the change.

Risk: Export commands can write report or review data to local files.

Mitigation: Use exports only with safe output paths and confirm the destination before sharing or reusing generated files.

## Reference(s):

- [Dedicated Operation Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-features)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown and concise text responses with optional shell commands and JSON API summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links, data scope, evidence gaps, credits used, and exported CSV, Markdown, or HTML paths when requested.]

## Skill Version(s):

1.4.8 (source: server release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
