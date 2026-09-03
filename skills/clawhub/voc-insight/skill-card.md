## Description:

VOC洞察 extracts customer voice from Amazon reviews, including personas, purchase motivations, usage scenarios, sentiment, unmet needs, Listing copy opportunities, and product improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to collect and analyze product reviews, then turn VOC findings into Listing optimization, product improvement, competitive comparison, alerting, export, and customer-response guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI credits may be spent automatically when the server-side auto-confirm policy allows low-cost or early-run paid actions.

Mitigation: Review the auto-confirm setting after setup, disable it when explicit approval is required, and check returned credit-use notes before continuing.

Risk: The ARI API key is stored locally and sent to ARI for authenticated requests.

Mitigation: Use the documented setup flow or ARI_API_KEY environment variable, do not include keys in reports or command examples, and clear unexpected custom endpoint environment variables.

Risk: Commands can change operational state, including monitoring schedules, competitor bindings, exports, and workbench review status.

Mitigation: Run read-only checks first and require clear user intent before executing state-changing commands.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [VOC洞察 README](artifact/README.md)
- [VOC洞察 ClawHub Skill Page](https://clawhub.ai/funewa/skills/voc-insight)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown and JSON responses, with optional CSV, Markdown, or HTML exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; some collection, analysis, monitoring, leaderboard, and advice workflows can consume ARI credits.]

## Skill Version(s):

1.4.5 (source: server release evidence, SKILL.md frontmatter, _meta.json, and CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
