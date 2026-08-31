## Description:

多商品批量生图流水线。商品清单 CSV -> 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, developers, and content teams use this skill to turn a SKU manifest and product images into a consistent batch image-generation workflow with retry, resume, budget controls, and output review artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompt text, and SKU details are sent to the configured image-generation provider.

Mitigation: Use only providers approved for the data being processed, avoid sensitive inputs, and review provider configuration before running batches.

Risk: Large SKU batches can consume credits quickly or run beyond the intended budget.

Mitigation: Run dry-run estimates first, set max-credit controls, start with one SKU and a small sample, then scale the batch.

Risk: Untrusted image URLs or manifests can pull unexpected content into the workflow.

Mitigation: Use trusted local files or vetted URLs and review manifest rows before execution.

Risk: Generated product images may vary in fidelity or platform compliance across SKUs.

Mitigation: Keep the visual specification fixed, sample-check outputs, use platform compliance checks where relevant, and rerun or review failed SKUs.

Risk: The bundled brand.yaml is a sample and may not match production brand requirements.

Mitigation: Edit brand.yaml for the actual brand, model references, photography rules, forbidden content, and target platform before production use.

## Reference(s):

- [Batch Image Skill Page](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI Reference](references/provider-cli.md)
- [seedream-5.0 Model Flags](references/model-flags.md)
- [Platform Image Specifications](references/platform-specs.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy Platform](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with shell, CSV, YAML, and JSON examples; script execution can produce image files, CSV/JSON manifests, and an HTML contact sheet.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run estimates, provider selection, retries, concurrency, resume state, max-credit controls, and optional platform compliance checks.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
