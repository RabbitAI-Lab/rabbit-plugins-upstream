## Description:

材质质感增强与纹理重建。糊掉的图 + 高清商品图 → 纹理清晰可信的图。当用户说「增强质感」「图糊了」「补纹理」「提清晰度」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to improve blurred apparel material texture in product imagery while preserving the subject, composition, garment silhouette, color, and background. It guides the agent through source and high-resolution reference image selection, prompt construction, command execution, and output review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image inputs and prompts may be sent to dLazy or another configured image provider.

Mitigation: Confirm the selected provider and its data handling are acceptable before processing confidential product imagery.

Risk: Remote image URLs supplied as inputs may be fetched from the user's network and passed to cloud providers.

Mitigation: Prefer trusted local image files, avoid internal or untrusted URLs, and run the tool in a sandbox or restricted network for sensitive projects.

Risk: The npx path depends on the dLazy CLI package selected at execution time.

Mitigation: Verify the dLazy CLI package before using the npx invocation path.

## Reference(s):

- [Material Enhancement Skill Page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands and optional JSON status output; generated assets are saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a source image plus a high-resolution product reference image; helper scripts can estimate credits, route providers, and save one or more enhanced JPEG outputs.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
