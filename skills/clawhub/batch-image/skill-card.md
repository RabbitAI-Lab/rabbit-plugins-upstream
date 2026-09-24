## Description:

多商品批量生图 Batch Image helps agents turn a product CSV into consistent ecommerce product images with shared visual specifications, controlled concurrency, retries, resume support, cost checks, and review outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and developers use this skill to generate batches of visually consistent product images from SKU manifests while preserving a fixed style specification across the batch. It also guides dry runs, sampling, retries, cost control, and post-run review before commercial use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and selected image files are sent to the configured image-generation provider.

Mitigation: Use only product data and images that may be shared with that provider, and review provider terms and credential handling before running jobs.

Risk: Large batch jobs can consume paid generation credits quickly.

Mitigation: Run --dry-run first, test one SKU and a small sample, and set batch cost controls such as --max-credits before full production runs.

Risk: Generated product images may be inaccurate or fail marketplace image requirements.

Mitigation: Keep the visual specification stable, sample and review outputs before full release, and use platform checks or manual review before publishing images.

Risk: Batch scripts write generated files, state files, manifests, and contact sheets to local output paths.

Mitigation: Choose a dedicated output directory and review generated paths before running or resuming batch jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0 model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration, files]

**Output Format:** [Markdown guidance with bash and Node.js command examples; helper scripts can emit JSON manifests, contact-sheet HTML, and image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch workflows may write generated assets, batch state, manifests, and contact sheets to local output paths.]

## Skill Version(s):

1.0.13 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
