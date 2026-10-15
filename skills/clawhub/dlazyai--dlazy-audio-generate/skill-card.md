## Description:

Selects dLazy audio models to generate speech, music, and sound effects from user requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select dLazy commands for text-to-speech, music, dialogue, and sound-effect generation through a hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audio-focused skill also describes non-audio commands and media uploads.

Mitigation: Review before installing for audio-only workflows; run only user-requested audio commands and selected files.

Risk: Prompts and supplied local image, video, or audio files may be sent to dLazy's hosted service.

Mitigation: Confirm intended uploads with the user and avoid private paths unless the user explicitly approves sharing those files.

Risk: A dLazy API key is stored locally when signing in.

Mitigation: Protect the credential and revoke or rotate it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI repository (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and generated audio URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; the CLI returns result URLs.]

## Skill Version(s):

1.3.30 (source: ClawHub release; bundled skill frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
