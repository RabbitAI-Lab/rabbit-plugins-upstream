## Description:

不压库存选品专家 helps light-asset Amazon sellers find FBM product opportunities with low inventory pressure, using sales, listing age, fulfillment, sorting, deduplication, and ASIN scoring workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to identify FBM, self-fulfilled product candidates that match monthly sales, recent listing, and low inventory-pressure constraints. It can also guide follow-up ASIN scoring and scheduled product selection workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package bundles broader automation and agent-modifying tools beyond the main Amazon product selection workflow.

Mitigation: Before installation, review or remove unrelated nested skills and the agent-modifying patching script.

Risk: The skill may need a LinkFox API key, local file-write access, public file upload capability, and optional scheduled-task authority.

Mitigation: Install only for trusted LinkFox use, keep gateway environment variables pinned to trusted hosts, and explicitly approve scheduled tasks or public uploads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-low-inventory-product-selection)
- [Amazon product scout API parameters](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [ASIN scoring expectations example](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [Task scheduler API](artifact/skills/linkfox-task-scheduler/references/api.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown conversation output with Excel (.xlsx) files, file paths, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Top 10 previews, Excel exports, scoring summaries, sorting prompts, and optional scheduled-task setup guidance]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
