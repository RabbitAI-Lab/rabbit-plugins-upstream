## Description:

Generates videos from text and optional image, video, or audio references, including first and last frame inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate short videos from prompts, reference media, or first and last frame images, and receive generated media links or saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference images, video, or audio are uploaded to dLazy for generation.

Mitigation: Use only media you are comfortable uploading to dLazy.

Risk: Login stores an organization API key in the local CLI configuration.

Mitigation: Keep the key private and rotate or revoke it when it is no longer needed.

Risk: Video generation can incur costs.

Mitigation: Review the generation cost with --dry-run before submitting a request.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [JSON result with generated media URLs, or a saved media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a task identifier for asynchronous generation; media can be saved to a local path.]

## Skill Version(s):

1.3.34 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
