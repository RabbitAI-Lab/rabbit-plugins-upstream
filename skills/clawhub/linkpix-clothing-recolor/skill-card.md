## Description:

一键生成服装的不同颜色版本，保持版型、材质及光影一致，无需重新拍摄即可完成 SKU 色卡图制作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, merchandisers, and agents use this skill to generate additional color variants of clothing product photos for SKU color cards without a new photoshoot. It guides qhkit/LinkPix image generation, model selection, credit confirmation, and result delivery for clothing recoloring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents to install or upgrade local qhkit, Node, or related image tooling.

Mitigation: Review installation commands before execution and prefer existing trusted package management or npx fallback when global install permissions are unavailable.

Risk: The workflow may upload clothing images to qhkit/LinkPix and consume service credits.

Mitigation: Confirm model, image count, image references, dimensions, and estimated credits with the user before any generate action.

Risk: The workflow may require configuring a qhkit API token.

Mitigation: Use a secure local or platform credential mechanism for the API key instead of pasting secrets into chat.

Risk: Generated recolors are not pixel-level edits and may alter product details such as text, logos, or garment structure.

Mitigation: Have the user review generated images for key product details before publishing SKU imagery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-clothing-recolor)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix/Qinghu service](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-facing confirmation prompts, qhkit commands, configuration guidance, and generated image delivery notes.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
