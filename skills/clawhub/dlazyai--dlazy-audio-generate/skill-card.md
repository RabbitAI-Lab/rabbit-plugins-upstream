## Description:

Selects a dLazy audio model to generate speech, music, or sound effects from a user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and run dLazy audio generation or text-to-speech commands for voiceovers, dialogue, music, and sound effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy-hosted services.

Mitigation: Share only content you are comfortable sending to dLazy and review the request before running it.

Risk: Using the dLazy CLI requires an external package and an API key.

Mitigation: Review the package before installation, use the pinned npx command if you prefer no global install, and rotate or revoke the API key when needed.

## Reference(s):

- [ClawHub audio generation skill](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with CLI commands and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results can include audio URLs or voice previews.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
