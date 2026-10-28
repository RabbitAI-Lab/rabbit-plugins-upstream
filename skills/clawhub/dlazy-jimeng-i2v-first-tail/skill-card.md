## Description:

Generate coherent transition videos from first and last frame images using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to make a transition video from a prompt and supplied first and last frame images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media files are sent to dLazy for cloud processing and storage.

Mitigation: Only submit prompts and media you are comfortable uploading to dLazy.

Risk: Authentication normally stores the dLazy API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

Risk: Video generation may incur costs.

Mitigation: Use --dry-run to review the payload and cost estimate before generating.

Risk: The examples use --image although the documented options name --firstFrame and --lastFrame.

Mitigation: Check the command help and use its current documented frame options.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Hosted video URL with JSON generation result or task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video duration is 5 or 10 seconds; asynchronous tasks may return a task identifier before completion.]

## Skill Version(s):

1.3.35 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
