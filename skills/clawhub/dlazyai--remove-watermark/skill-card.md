## Description:

去水印去文字。带水印 / 文字 / logo 的图 → 干净图，背景纹理自然补全。当用户说「去水印」「去文字」「擦掉 logo」「把字去了」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce content creators use this skill to remove watermarks, promotional text, and decorative overlays from images they are authorized to edit, reconstructing covered areas for downstream image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts are sent to the selected cloud provider for processing and may contain confidential content.

Mitigation: Select an approved provider, preview with --dry-run, and do not send confidential images unless the provider is approved for that data.

Risk: Reconstructed areas are model-inferred and nearby image details or perspective may change.

Mitigation: Review the result and important occluded details before use; use professional pixel-level editing when exact preservation is required.

Risk: Removing watermarks, brand marks, or legal labels without authorization can enable misuse.

Mitigation: Only edit images you are authorized to modify, and do not remove others’ copyright watermarks, brand identifiers, or legally required labels.

Risk: Cloud image generation can incur API charges or save output over an existing file.

Mitigation: Preview with --dry-run, expect provider charges, and choose a separate output path.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG image output with Markdown usage instructions and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image edits are generative reconstructions and may alter covered or nearby details; inspect results before use.]

## Skill Version(s):

1.0.25 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
