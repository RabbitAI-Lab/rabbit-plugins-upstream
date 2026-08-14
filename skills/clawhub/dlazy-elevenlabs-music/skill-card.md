## Description:

Generates 10-300 second original music from a natural-language prompt using ElevenLabs music_v1 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short original music tracks for background music, ads, and short-video soundtracks from natural-language prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generated output metadata are sent to dLazy as a cloud provider.

Mitigation: Confirm the user is comfortable using dLazy before generation and avoid submitting sensitive prompt content unless approved.

Risk: Authentication may save a dLazy API key in the local CLI configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY option when local persistence is not desired, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Installing the CLI globally persists a third-party binary on the system.

Mitigation: Use the pinned npx form when a global install is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated music output URLs are hosted by dLazy; asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
