## Description:

This skill helps Douyin Shop sellers and ecommerce teams generate product main images, carousel sets, detail images, short-video covers, live-commerce inserts, and promotional images through Qinghu AI and the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, short-video teams, and live-commerce teams use this skill to prepare Douyin-oriented product visuals from product images and campaign copy. The skill guides an agent through qhkit options, estimation, generation, image-size handling, and delivery for main-image sets, detail pages, and campaign posters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Qinghu API tokens may be exposed if pasted directly into chat or retained in logs.

Mitigation: Use a dedicated low-scope token, prefer a platform secret manager or environment variable, and rotate the token after use when exposure is possible.

Risk: The skill can install or upgrade qhkit from broad or latest package sources, which may change behavior over time.

Mitigation: Review the package before installation and prefer a pinned, local, or sandboxed qhkit installation where operational policy requires reproducibility.

Risk: Image generation consumes credits and submitted jobs may not be cancellable.

Mitigation: Run qhkit estimate when supported and require explicit user confirmation of model, image count, size, quality, references, and expected credits before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-douyin-shop-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage from qhkit after user-confirmed generation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
