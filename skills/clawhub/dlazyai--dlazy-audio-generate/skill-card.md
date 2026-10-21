## Description:

Selects a dLazy audio model for text-to-speech, dialogue, music, or sound effects based on the user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and run dLazy audio-generation commands for speech, dialogue, music, and sound effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files explicitly provided to the CLI may be sent to dLazy's hosted service.

Mitigation: Only submit content you are comfortable sharing with dLazy.

Risk: Logging in stores an API key in the local user configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: A global CLI installation persists on the system.

Mitigation: Use the pinned npx invocation if you prefer not to keep a global installation.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands; CLI returns JSON with generated audio URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and access to its hosted service.]

## Skill Version(s):

1.3.33 (source: ClawHub release metadata; artifact frontmatter lists 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
