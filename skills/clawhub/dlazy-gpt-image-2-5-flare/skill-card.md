## Description:

Helps agents generate and edit images using the dLazy GPT Image 2.5 Flare CLI, with reference images, multiple aspect ratios, and quality settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users create or edit images from text prompts and optional reference images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference images are sent to dLazy's cloud service.

Mitigation: Only include prompts and local files you intend to share with dLazy.

Risk: The CLI may store the dLazy API key locally.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: A global CLI installation remains on the system after use.

Mitigation: Use the documented npx invocation if a persistent installation is not wanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [Publisher-provided CLI homepage](https://github.com/dlazy-ai/cli)
- [Publisher-provided npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with generated image URLs; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation and optional local download.]

## Skill Version(s):

1.2.21 (source: server-resolved ClawHub release; bundled skill frontmatter states 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
