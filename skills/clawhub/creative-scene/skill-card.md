## Description:

Creative Scene helps agents generate original ecommerce-style images from a text description or revise a reference image for model, pose, or styling changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, and agents use this skill to create product and editorial scene images from prompts, then make targeted model, pose, and outfit edits using optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any reference images may be sent to the configured image provider.

Mitigation: Avoid private or sensitive prompts and image URLs, and confirm the selected provider before execution.

Risk: Provider credentials and custom provider binaries can change where requests are routed.

Mitigation: Use doctor or dry-run mode to verify routing, and set provider API keys or DLAZY_BIN only in controlled environments.

Risk: Generated images could be misused for specific-person likenesses, inappropriate minor-related content, or misleading product imagery.

Mitigation: Follow the skill's stated exclusions and review outputs before commercial use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider CLI Reference](references/provider-cli.md)
- [banana-pro Model Flags](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved as JPEG files; dry-run mode can output a request summary before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
