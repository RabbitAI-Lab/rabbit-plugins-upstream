## Description:

Converts one product image and selling points into a consistent set of e-commerce product images across multiple angles, scenes, and compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agent developers use this skill to turn a single product reference image plus selling points into a full product image set for listings and detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and optional brand references may be sent to cloud image providers.

Mitigation: Use dry-run first, choose a trusted provider, and use scoped, revocable API keys.

Risk: Generated files are written to caller-provided save paths.

Mitigation: Review save paths before running generation and keep outputs in an expected project directory.

Risk: Generated e-commerce images may drift from the reference product or imply unsupported product features.

Mitigation: Compare the full image set against the source product and selling points before publishing; regenerate any image that changes product shape, color, material, or claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Model flags reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration, image files]

**Output Format:** [Markdown guidance with bash and Node.js command examples, configuration snippets, and generated image file paths or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved locally when a save path is provided; dry-run mode can preview provider requests without generation.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
