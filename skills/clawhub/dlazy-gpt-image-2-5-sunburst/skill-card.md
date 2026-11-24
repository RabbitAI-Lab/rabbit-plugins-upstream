## Description:

Generate and edit detailed images with GPT Image 2.5 Sunburst using text prompts, optional reference images, aspect ratios up to 21:9, and quality settings up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative professionals and other agent users can generate new images or edit supplied images with detailed prompts, reference images, aspect ratios, and quality settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial scan reported authentication-only behavior that may not match the skill's image-generation purpose.

Mitigation: Review the CLI help and setup flow, and confirm the expected generation behavior before relying on the skill.

Risk: Prompts and supplied local reference images are sent to dLazy hosted services.

Mitigation: Avoid submitting sensitive prompts or images unless the service is approved for that content.

Risk: The skill requires a dLazy API key, which is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the key, avoid exposing it in logs or shared environments, and rotate or revoke it if needed.

## Reference(s):

- [dLazy CLI source (listed by the skill)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON metadata]

**Output Format:** [Image files with JSON output metadata and hosted result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to 5 reference images; supports aspect ratios up to 21:9 and quality levels from low to max; can save results locally or return an asynchronous task ID.]

## Skill Version(s):

1.2.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
