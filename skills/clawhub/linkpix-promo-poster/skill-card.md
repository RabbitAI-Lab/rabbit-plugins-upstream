## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）快速生成双11、黑五、圣诞节等营销活动海报与折扣营销图，适用于新品发布、促销活动及品牌宣传。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to guide an agent through generating promotional posters, discount marketing images, and launch visuals with qhkit. It covers setup, model and size selection, cost estimation, generation, delivery, and common failure handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to make persistent toolchain changes, including installing qhkit or Node globally.

Mitigation: Review before installing in shared or production environments and prefer a pre-provisioned qhkit binary.

Risk: The skill may automatically reuse a root-level qhkit credential file.

Mitigation: Use a scoped token supplied for this skill and avoid root-level credential reuse unless it is an intentional platform policy.

Risk: Generated poster text, numbers, logos, or product details may be inaccurate.

Mitigation: Review generated images before delivery and regenerate when key copy, numeric offers, logos, or product structure are wrong.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-promo-poster)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit image-generation requests, generated image URLs, and actual credit usage returned by the CLI.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
