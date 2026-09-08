## Description:

A professional product image generation skill for Amazon product detail pages, covering main images, secondary images, and A+ Brand Content modules designed around Amazon image guidelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and creative teams use this skill to plan and generate Amazon-ready product image sets, including a compliant main image, secondary marketing images, and A+ content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on installing and executing a third-party CLI.

Mitigation: Review the dLazy CLI package and source provenance, prefer on-demand execution with a pinned version, and run it in a restricted environment.

Risk: API credentials may be stored persistently in the local dLazy configuration.

Mitigation: Use the DLAZY_API_KEY environment variable when practical and rotate or revoke keys from the dLazy dashboard after use.

Risk: Prompts and selected local media can be sent to dLazy API and file services.

Mitigation: Avoid sensitive prompts or media unless the data-sharing posture has been approved for the intended use.

Risk: Prompt-derived shell commands can affect the local environment if run without review.

Mitigation: Inspect each generated command before execution and avoid global installation when a scoped or temporary invocation is sufficient.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Image URLs]

**Output Format:** [Markdown with inline shell commands, checklists, confirmation prompts, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow may request user confirmation between generation steps and typically produces one image result per CLI invocation.]

## Skill Version(s):

1.3.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
