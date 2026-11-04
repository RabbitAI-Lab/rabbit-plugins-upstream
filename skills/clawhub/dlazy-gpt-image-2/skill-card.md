## Description:

GPT Image 2 skill for generating images from text prompts and editing or synthesizing images with reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the dLazy CLI to generate images from prompts or edit and combine images with reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy, and use may incur service charges.

Mitigation: Use the service only if you accept those data transfers and charges; use --dry-run to review the estimate before generating when appropriate.

Risk: The CLI stores an organization API key locally and may upload local image files.

Mitigation: Protect the saved API key and provide only files you intend to upload.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands]

**Output Format:** [JPEG, PNG, or WebP image files with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a text prompt, optional reference images, and image size, format, and quality settings; images can be saved locally.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
