## Description:

Generates coherent transition videos from supplied first and last frames using Jimeng's video generation model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate a transition video from a prompt and supplied first and last frame images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial with medium confidence and unresolved local references; its summary says the supplied evidence does not demonstrate the stated video-generation behavior.

Mitigation: Review the pinned @dlazy/cli package and confirm the command and output behavior before installing or using it.

Risk: The skill requires a dLazy API key, and local image files passed to the CLI are uploaded to dLazy media storage while prompts and parameters are sent to its hosted API.

Mitigation: Keep API keys private and avoid sending confidential or personal media unless it is approved for external processing; rotate or revoke a key if exposed.

## Reference(s):

- [dLazy CLI on GitHub](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON, Media URLs]

**Output Format:** [JSON result with generated media URLs or asynchronous task status; optionally saved media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous tasks can return a task ID before the media is ready.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
