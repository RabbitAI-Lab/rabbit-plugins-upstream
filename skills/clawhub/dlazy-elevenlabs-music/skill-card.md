## Description:

Generates 10-300 second original music with ElevenLabs music_v1 from a natural-language prompt for background music, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to ask an agent to generate short original music through the dLazy CLI and receive hosted output URLs or an optional saved file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files explicitly passed to the skill may be uploaded to a third-party hosted API.

Mitigation: Avoid sensitive prompts or files unless third-party processing is approved for the use case.

Risk: Login stores a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY where appropriate and rotate or revoke the key when access should end.

Risk: A global CLI install persists a third-party executable on the system.

Mitigation: Use the pinned npx command for on-demand execution when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance plus JSON results containing generated asset URLs and optional local saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
