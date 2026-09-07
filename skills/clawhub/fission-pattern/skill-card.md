## Description:

Generates a coordinated e-commerce image set from one product photo and selling points, with multiple angles, use scenes, and detail shots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and developers use this skill to turn a clean product image plus product attributes into prompts and commands for a consistent product photo set suitable for main images and detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be uploaded to the configured image provider.

Mitigation: Use approved providers, avoid sensitive product assets unless permitted, and review provider data handling before execution.

Risk: Running generation commands may consume provider credits.

Mitigation: Use the dry-run option first to inspect the request and expected cost before generating images.

Risk: Generated images may alter product details or imply unsupported product features.

Mitigation: Review the completed image set for product fidelity, consistent appearance, absent watermarks, and only supported selling claims before publication.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Fission Pattern on ClawHub](https://clawhub.ai/dlazyai/skills/fission-pattern)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, bash command examples, and optional JSON envelopes from generation scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated image files locally when commands are executed; dry-run can inspect requests without generating images.]

## Skill Version(s):

1.0.6 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
