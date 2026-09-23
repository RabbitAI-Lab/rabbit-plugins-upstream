## Description:

Generates macro e-commerce detail images from apparel photos, focusing on fabric texture, stitching, weave, and garment construction details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, designers, and content agents use this skill to turn standard apparel product photos into close-up detail images for product pages. It is intended for visible garment details such as collars, cuffs, hems, buttons, zippers, embroidery, prints, weave structure, and fabric fibers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apparel images, prompts, and generated outputs may be sent to the configured cloud image provider.

Mitigation: Choose a trusted provider explicitly, review that provider's data policy, and avoid confidential or regulated imagery unless the policy allows it.

Risk: Generation can consume paid credits.

Mitigation: Run the skill in dry-run mode first and confirm provider, model, image size, quality, batch count, and estimated cost before execution.

Risk: Low-resolution, compressed, or obstructed source photos can lead to invented or inaccurate garment details.

Mitigation: Use clear high-resolution source images, enlarge one target area per prompt, preserve color and structure in the prompt, and review outputs for fabricated construction details.

Risk: Provider credentials are required for non-dry-run execution.

Mitigation: Use normal provider authentication flows or environment variables, keep keys out of prompts and committed files, and rotate or revoke keys according to provider policy.

## Reference(s):

- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-detail)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands; command execution can produce JSON status and saved JPEG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses high-quality image generation, supports dry-run cost checks, and can save batched outputs with numbered filenames.]

## Skill Version(s):

1.0.12 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
