## Description:

Generates images from text prompts and edits or synthesizes images using reference images through dLazy's GPT Image 2 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate images from prompts or edit and synthesize images with reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented login flow stores an API key in the local CLI configuration.

Mitigation: Review the CLI package before authenticating, protect the local configuration, and rotate or revoke the key if needed.

Risk: The security review was partial and noted hidden whitespace in the skill text; the npm package and some referenced paths were not inspected.

Mitigation: Review the padded section and unresolved paths, and inspect the npm package before installing or running the CLI.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files and a JSON result containing image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID before image outputs are ready.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
