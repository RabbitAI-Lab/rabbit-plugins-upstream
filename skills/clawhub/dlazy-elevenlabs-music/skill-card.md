## Description:

ElevenLabs music_v1 generates 10-300 second original music from natural-language prompts for BGM, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short original music tracks from text prompts through dLazy's hosted ElevenLabs Music wrapper. Typical uses include background music, advertising music, and short-video soundtracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files explicitly passed to the skill are sent to dLazy/ElevenLabs cloud services.

Mitigation: Use only content appropriate for that service and review data-sharing expectations before generation.

Risk: The dLazy API key is a credential that may be saved in local CLI configuration or supplied through DLAZY_API_KEY.

Mitigation: Protect the key, limit local exposure where possible, and rotate or revoke it from the dLazy dashboard if needed.

Risk: A global npm install persists the dLazy CLI on the system.

Mitigation: Use the pinned npx command when a non-persistent CLI invocation is preferred.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON responses containing generated output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted file URLs; asynchronous runs may return a generation ID for polling.]

## Skill Version(s):

1.3.7 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
