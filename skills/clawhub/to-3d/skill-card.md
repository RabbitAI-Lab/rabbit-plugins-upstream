## Description:

平铺图转隐形模特立体图。平铺图 → 有体积感与版型的立体展示图。当用户说「转 3D」「立体图」「隐形模特」「把衣服撑起来」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and e-commerce teams use the skill to turn a flat-lay clothing photo into a dimensional ghost-mannequin product image while guiding garment shape, detail, and framing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clothing photos and prompts are sent to the selected cloud image provider, and the provider's retention practices are not verified.

Mitigation: Choose the provider explicitly and review its data handling terms before submitting confidential designs.

Risk: The external CLI version and its behavior are not verified.

Mitigation: Use a reviewed CLI version and save generated files to a dedicated output path.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 options](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG image files with Markdown instructions and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates dimensional product images from user-supplied clothing photos and prompts; supports square or portrait output and optional batch generation.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
