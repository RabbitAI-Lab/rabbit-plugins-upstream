## Description:

从零创意生图，也可定向改模特、姿势、搭配。一句描述（可选参考图）→ 图。当用户说「创意生图」「生成一张」「改个姿势」「换模板」「随便来张图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can create concept, editorial, and ecommerce images from text prompts, or edit a supplied reference image to change a model, pose, or outfit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image prompts and optional reference images are sent to a cloud provider, and generation may incur API charges.

Mitigation: Choose the intended provider and preview the request with --dry-run before generating; avoid sending private reference images unless appropriate.

Risk: Generated files may overwrite or mix with other local outputs, and external CLI behavior or provider retention practices are not verified.

Mitigation: Use a dedicated output path and a reviewed CLI version; check the provider's current handling terms before sending sensitive material.

## Reference(s):

- [Provider CLI and data flow](references/provider-cli.md)
- [banana-pro model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [Creative Scene on ClawHub](https://clawhub.ai/dlazyai/skills/creative-scene)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Prompt guidance]

**Output Format:** [Generated image files, with Markdown prompt templates and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image dimensions and aspect ratio vary by request; outputs are saved to a user-selected path. Reference images can be used for edits.]

## Skill Version(s):

1.0.29 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
