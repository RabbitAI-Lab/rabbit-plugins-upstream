## Description:

Alibaba Bailian qwen-image-2.0-pro generates images from prompts, with support for complex text, multi-line layouts, photorealistic detail, and semantic adherence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to generate images from text prompts, optionally guided by reference images, for mixed text and image designs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference files are sent to dLazy for generation.

Mitigation: Review the CLI and avoid submitting sensitive prompts or files.

Risk: Image generation can consume service credits.

Mitigation: Use the CLI dry-run option to review the request and cost estimate before generation.

Risk: Login stores a reusable dLazy API key in local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [PNG image with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image dimensions are selectable; asynchronous requests may return a task identifier before the image is ready.]

## Skill Version(s):

1.3.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
