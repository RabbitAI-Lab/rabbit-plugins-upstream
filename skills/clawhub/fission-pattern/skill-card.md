## Description:

Fission Pattern helps agents turn one product image plus selling points into prompt sets and shell commands for consistent multi-angle e-commerce product imagery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and developers use this skill to create consistent product-photo sets for storefront main images and detail pages from a single reference image. The skill guides prompt construction, provider selection, command execution, and output review for product fidelity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product images may be sent to cloud image-generation providers.

Mitigation: Use non-confidential product images and review provider data handling before running generation commands.

Risk: Image inputs can be local paths or URLs, including URLs chosen outside the skill author's control.

Mitigation: Use trusted local files or public HTTPS URLs, and do not let untrusted content choose image input values.

Risk: Alternate provider endpoints can expose credentials or image data if misconfigured.

Mitigation: Set ARK_BASE_URL only for endpoints you control and trust with the relevant API key.

Risk: Generated image sets may drift from the reference product or imply unsupported product claims.

Mitigation: Review the full set before publication for product fidelity, claim accuracy, text artifacts, and watermark artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash command examples and generated image file paths or URLs from provider CLIs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include prompts, dry-run request summaries, JSON status from generation commands, and saved image paths.]

## Skill Version(s):

1.0.8 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
