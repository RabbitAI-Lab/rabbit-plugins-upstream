## Description:

Generates multilingual ElevenLabs eleven_v3 speech with selectable voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to turn text into multilingual speech for dubbing, audiobooks, and character dialogue, with controls for voice selection, stability, similarity, and style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text and supplied media are sent to dLazy for cloud processing, and generation may consume account credits.

Mitigation: Use only content you are comfortable sending to dLazy, and consider credit use before requesting generation.

Risk: The dLazy API key is stored in the local CLI configuration.

Mitigation: Protect the stored key and rotate or revoke it if exposed.

Risk: The pinned CLI implementation was not audited as part of this release review.

Mitigation: Review the pinned CLI before installing it.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio files]

**Output Format:** [Generated audio asset, returned as a URL or saved to a local path]

**Output Parameters:** [1D (text to speech)]

**Other Properties Related to Output:** [Voice selection and stability, similarity, and style controls; generation can return asynchronously.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
