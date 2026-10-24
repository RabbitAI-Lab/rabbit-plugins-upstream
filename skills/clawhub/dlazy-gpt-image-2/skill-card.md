## Description:

Generates images from text prompts and edits or synthesizes images using supplied reference images with GPT Image 2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create images from text prompts and to edit or synthesize images with reference inputs. The service requires sending prompts and any supplied images to dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy's hosted API and media storage.

Mitigation: Use only prompts and images you are comfortable uploading to dLazy.

Risk: Authentication can store an API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable when you do not want the key saved locally, and rotate or revoke exposed keys.

Risk: Image generation may incur service charges.

Mitigation: Check account charges and available credits before generating images.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project homepage (skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, Generation metadata]

**Output Format:** [Generated image files (JPEG, PNG, or WebP) and JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images can be generated from text prompts or edited using reference images.]

## Skill Version(s):

1.3.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
