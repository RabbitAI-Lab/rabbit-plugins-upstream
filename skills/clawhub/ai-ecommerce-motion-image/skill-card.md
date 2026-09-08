## Description:

Guides e-commerce teams through using AI-HIVE MCP to turn authorized static product images into short looping product-motion samples with prompts, JSON work orders, acceptance checks, and rollback criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce merchants, content teams, agencies, and advertising teams use this skill to create AI-assisted product motion-image samples from authorized SKU assets. It helps plan a pilot-first workflow, capture cost and task metadata, check product fidelity and platform requirements, and decide when to stop or roll back.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can be used with product assets whose ownership, brand rights, or talent rights are unclear.

Mitigation: Require owned or authorized reference assets, approved briefs, and human approval before generating or publishing media.

Risk: AI-HIVE tools, model availability, prices, or task fields may change after the skill is installed.

Mitigation: List available tools and confirm current pricing and task status before each run; record a cost snapshot with every result.

Risk: Generated motion can alter product shape, logo, label text, color, materials, accessories, or platform-safe layout.

Mitigation: Run a pilot sample first, inspect frames against the source SKU, and stop or roll back when fidelity or platform requirements fail.

Risk: The activation description may route broad shopping, marketplace, or generic image requests into this specialized workflow.

Mitigation: Narrow activation to authorized e-commerce product motion-image requests involving AI-HIVE MCP or equivalent product-media workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-motion-image)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown guidance with prompt templates, JSON work-order examples, acceptance criteria, and stop conditions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing workflow guidance; it does not include an executable installer.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
