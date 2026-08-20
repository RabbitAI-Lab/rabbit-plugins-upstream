## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）一站式生成电商营销素材：商品主图、场景图、详情页、促销海报、广告图片与广告视频，覆盖商品包装、活动推广和品牌营销。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing operators use this skill to ask an agent to plan and generate ecommerce marketing asset batches, including product images, detail-page images, promotional posters, and advertising videos through the qhkit CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade global Node tooling as part of setup.

Mitigation: Review setup commands before execution and prefer an existing approved qhkit installation or a user-approved npx fallback when global installation is not appropriate.

Risk: The skill may reuse an existing qhkit token configuration.

Mitigation: Confirm the intended account and environment before running commands that use stored credentials.

Risk: The skill may upload local product images or videos to the LinkPix/qhkit service.

Mitigation: Use only media that is approved for upload to that provider and confirm upload scope before generation.

Risk: The skill can spend credits after estimating generation cost.

Mitigation: Run estimates first and require user confirmation before submitting paid generation jobs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-marketing-assets)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs, task IDs, credit estimates, and setup or upgrade instructions for qhkit.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
