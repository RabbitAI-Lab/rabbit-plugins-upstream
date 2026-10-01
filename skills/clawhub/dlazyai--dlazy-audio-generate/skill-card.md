## Description:

Selects a dLazy audio model to generate speech, music, or sound effects from user prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate voiceovers, dialogue, music, and sound effects through dLazy's hosted audio models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy for generation.

Mitigation: Review inputs before submission and avoid sharing sensitive content.

Risk: Login can persist an API key in the local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key from the dLazy dashboard if needed.

Risk: A global CLI installation persists on the user's machine.

Mitigation: Use the documented pinned npx invocation instead if a global install is not desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Audio URLs]

**Output Format:** [JSON results with links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is hosted by dLazy; requests require an API key.]

## Skill Version(s):

1.3.24 (ClawHub release; skill frontmatter: 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
