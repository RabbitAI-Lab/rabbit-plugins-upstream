## Description:

ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and controls for stability, similarity, and style, for dubbing, audiobooks, and character dialogue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn text into multilingual speech for dubbing, audiobooks, and character dialogue, choosing a curated or custom voice and tuning delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text and explicitly supplied media are processed in the dLazy cloud, and generation may incur credit charges.

Mitigation: Check billing and data handling expectations before submitting content.

Risk: The CLI stores credentials locally, and the security review does not certify the external CLI implementation.

Mitigation: Use device login, review the pinned CLI package before installation, and revoke saved keys when no longer needed.

## Reference(s):

- [CLI repository link declared in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, Asset URLs]

**Output Format:** [Generated audio asset URL in a JSON response; optionally a downloaded audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice selection and stability, similarity, and style controls; optional asynchronous status and local save.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
