## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）根据一张服装模特图自动生成多种姿势及展示角度的套图，丰富商品展示效果，适用于服装详情页及社交媒体营销。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce content teams use this skill to generate multi-pose, multi-angle apparel model image sets from a source model photo for product detail pages and social media marketing. The skill guides an agent through qhkit image generation, option lookup, credit estimation, polling, and delivery of generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that the workflow can perform persistent host installs and reuse local qhkit credentials.

Mitigation: Use a controlled environment with qhkit pre-provisioned, and only reuse local tokens when that is intended.

Risk: The workflow uploads source images to the qhkit/LinkPix service and may spend generation credits.

Mitigation: Run it only after the user explicitly requests multi-pose or multi-angle model image generation and accepts image upload and credit usage.

Risk: Generated apparel images may vary from the source photo in details such as text, logos, or garment structure.

Mitigation: Have the user review key product details before using generated images in commercial listings or marketing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-pose-set)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit commands and user-facing delivery guidance; generated image URLs are returned by the external qhkit/LinkPix service.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
