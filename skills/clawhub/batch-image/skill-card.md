## Description:

多商品批量生图流水线。商品清单 CSV → 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketers, and developers use this skill to turn a CSV product manifest into a batch of visually consistent product images, with retry, resume, cost controls, output manifests, and optional listing checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected cloud generation provider.

Mitigation: Use the skill only with providers approved for the product data being processed, and avoid including sensitive or confidential product material unless that provider is acceptable.

Risk: Malformed CSV values can cause outputs to be written outside the intended output folder.

Mitigation: Use trusted manifests, restrict SKUs to simple safe identifiers, and run the workflow in a contained project directory.

Risk: Generated contact-sheet HTML may include unescaped manifest values.

Mitigation: Avoid opening contact sheets from untrusted manifests until HTML escaping is fixed or the inputs have been reviewed.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [seedream-5.0 Model Flags](references/model-flags.md)
- [Platform Image Specifications](references/platform-specs.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/batch-image)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline shell commands, plus generated image files, JSON envelopes, batch manifests, state files, and optional contact-sheet HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may include local JPEG files, batch-manifest.json, .batch-state.json, per-run manifest JSON, and listing-check reports.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
