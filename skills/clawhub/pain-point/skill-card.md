## Description:

The pain-point skill uses ARI Amazon review data to extract customer pain points, unmet needs, trends, supporting review evidence, and practical product or listing recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to analyze review samples for buyer complaints, unmet needs, review-backed trends, competitor differences, and product or listing improvement priorities. It can also guide ARI authorization, credit-aware review analysis workflows, monitoring, reports, and exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI workflows can spend account credits for review collection, reports, analysis, advice, or category ranking.

Mitigation: Set the account to ask before every paid action when per-run consent is required, use quote-only flows for pricing, and confirm credit-spending actions explicitly.

Risk: Some workflows can change ARI account or workflow state, including monitoring, schedules, autoconfirm settings, competitors, alerts, and workbench status.

Mitigation: Review state-changing requests before execution and limit the agent to actions the user has clearly requested.

Risk: Exports can write local CSV, Markdown, or HTML files.

Mitigation: Choose a narrow export directory and filename, avoid broad directories such as the home folder, and avoid overwriting existing files.

Risk: The skill requires an ARI API key for authenticated workflows.

Mitigation: Use the ARI authorization flow or environment variable handling, do not paste secrets into reports or examples, and install only when granting this credential is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/pain-point)
- [funewa publisher profile](https://clawhub.ai/user/funewa)
- [README](README.md)
- [Usage guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Conversational text and Markdown, with optional exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Outputs are based on ARI-collected Amazon review samples and may involve credit-spending workflows.]

## Skill Version(s):

1.4.11 (source: server evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
