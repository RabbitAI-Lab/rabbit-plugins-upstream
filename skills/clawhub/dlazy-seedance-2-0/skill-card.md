## Description:

Generates videos with Seedance 2.0 from text prompts, multimodal references, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate videos from text prompts, reference images, video, or audio, and to control clips with first and last frames. They can choose resolution, aspect ratio, duration, and audio generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy services, and local media files may be uploaded for generation.

Mitigation: Submit only prompts and media you are comfortable sharing with dLazy; use the documented dry-run option to preview requests and costs.

Risk: Authentication can save an API key in the local CLI configuration.

Mitigation: Protect access to the local account and rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [dLazy CLI project information listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Media files, API Calls, JSON]

**Output Format:** [Generated video assets with a JSON result containing output URLs and metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video outputs are hosted at returned URLs and can optionally be saved locally; asynchronous jobs can return a task identifier before the output is ready.]

## Skill Version(s):

1.3.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
