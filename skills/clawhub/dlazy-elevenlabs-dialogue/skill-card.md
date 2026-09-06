## Description:

Generates multi-voice ElevenLabs eleven_v3 dialogue by assigning voices to dialogue lines and returning generated audio through the dLazy CLI service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create character dialogue, podcast segments, and short skits with multiple voices through a hosted audio-generation workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text is sent to dLazy for generation, and generated audio URLs are hosted remotely.

Mitigation: Avoid submitting sensitive or restricted dialogue unless dLazy's hosted service is approved for that content.

Risk: A dLazy API key may be stored in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: The submitted markdown contains stale usage examples.

Mitigation: Check dlazy elevenlabs-dialogue -h before use and follow the current CLI option names.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source link from skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [CLI command output as JSON with generated audio URLs; optional saved audio file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimates and async task polling; generated asset URLs are hosted remotely.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
