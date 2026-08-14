## Description:

An Amazon product and niche-market unmet-demand mining skill for finding customer pain points, review-driven product gaps, improvement opportunities, and product concepts from demand gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, product researchers, and ecommerce operators use this skill to identify high-demand, low-satisfaction products, preview candidate ASINs, export Excel results, and optionally apply profile-driven scoring for prioritization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API credentials and can send feedback or uploaded files to external services.

Mitigation: Install only in trusted environments, protect LinkFox credentials, and avoid processing sensitive files unless external service use is approved.

Risk: The skill writes full product research and scoring results to local Excel and JSON files.

Mitigation: Store outputs in approved locations, review file contents before sharing, and remove exports that contain sensitive business research.

Risk: The bundled scheduler can create future automated agent tasks and may consume service credits.

Mitigation: Confirm schedule, task content, notification destination, and expected credit cost with the user before creating or modifying tasks.

Risk: The bundle includes agent-instruction editing capability.

Mitigation: Do not run the patching script unless the user explicitly intends to modify another agent's instructions and has reviewed the change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-unmet-demand-miner)
- [Primary skill definition](artifact/SKILL.md)
- [Amazon product scout API parameter catalog](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [ASIN dynamic scoring example expectations](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [SellerSprite product search API reference](artifact/skills/linkfox-sellersprite-product-search/references/api.md)
- [Task scheduler API reference](artifact/skills/linkfox-task-scheduler/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown conversation responses with tables, shell command snippets, JSON status summaries, and Excel file outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Top 10 previews and Excel exports are emphasized; scoring outputs include weighted scores, recommendation grades, and rejection reasons.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
