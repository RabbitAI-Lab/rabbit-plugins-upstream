## Description:

GPT Image 2 generates images from text prompts and edits or combines images using reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy CLI users can generate images from text prompts or edit and combine up to five reference images with GPT Image 2.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner reported a mismatch between the image-generation description and observed login behavior, and its analysis was partial with local references unresolved.

Mitigation: Review the flagged whitespace and install references, and confirm the CLI authentication behavior before installing.

Risk: Prompts and local reference images are sent to dLazy hosted services for processing.

Mitigation: Avoid sending sensitive prompts or images unless their use with the service is approved.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [CLI repository listed in skill metadata (not verified as release provenance)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response containing generated image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier before image outputs are ready.]

## Skill Version(s):

1.3.41 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
