## Description:

Creates Chinese ecommerce main images with selling-point text layout from a product image, product benefits, and promotion copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, designers, and agents use this skill to turn a product image plus verified feature and promotion copy into a square marketplace main image with readable Chinese text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional brand/reference assets may be sent to dlazy or another configured provider API.

Mitigation: Use only assets you have rights to process and avoid confidential unreleased images, internal URLs, or sensitive prompt content.

Risk: Generated ecommerce copy could imply unsupported product capabilities, false promotions, or absolute claims.

Mitigation: Verify feature claims and promotional terms before use, and avoid unsubstantiated or absolute wording.

Risk: Chinese text and small-layout readability can vary in generated images.

Mitigation: Keep copy short, generate batches when needed, inspect output at marketplace thumbnail size, and rerun with stricter text/layout constraints if readability fails.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro parameter list](references/model-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and optional JSON output from generation scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide creation of saved image files through configured cloud image-generation providers; default task settings use seedream-5.0-pro, 1:1 size, and 2k resolution.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
