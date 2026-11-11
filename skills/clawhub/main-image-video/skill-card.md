## Description:

Turns a single product image into a short product video with controlled camera movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use the skill to turn a product listing image into a short motion clip for a product page. It supports camera movement and subtle material motion while keeping the clip focused on the original product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags privacy and scope concerns and notes that some code was only partially inspected.

Mitigation: Review the partially inspected code before installation. Before sending images or prompts, confirm which configured provider receives them and that its data handling, access, and video-generation behavior are acceptable; use dry-run and a single-image trial first.

## Reference(s):

- [Video backend configuration](artifact/references/video-backends.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Product video ad skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/product-video-ad/skill.md)
- [Item repair skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/item-repair/skill.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Short MP4 video files and Markdown instructions with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically produces a 3–5 second product clip; storyboard mode can also create subtitles and intermediate files.]

## Skill Version(s):

1.0.27 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
