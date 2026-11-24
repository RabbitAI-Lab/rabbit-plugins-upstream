## Description:

Generates PixVerse C1 videos from text prompts, images, first and last frames, or reference media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to request PixVerse C1 video generations from text prompts or supplied images, including first and last frame workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This skill requires dLazy login or an API key, and the security scan notes that the reviewed material raises questions about this setup relative to the stated video-generation purpose.

Mitigation: Review the dLazy CLI and account permissions before authenticating, and use an API key that can be rotated or revoked.

Risk: Prompts and supplied local image, video, or audio files are sent to dLazy hosted services for generation.

Mitigation: Avoid sending sensitive prompts or media unless you are comfortable with the service handling them.

Risk: The security scan was partial and did not review referenced local paths or configuration details, so it does not establish the full behavior.

Mitigation: Review the CLI installation and relevant configuration behavior before use; treat the benign, medium-confidence verdict as limited to the material scanned.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [JSON result envelope with generated media URLs or an asynchronous task identifier]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media may be saved to a local path. Prompts and supplied local media are sent to dLazy hosted services.]

## Skill Version(s):

1.2.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
