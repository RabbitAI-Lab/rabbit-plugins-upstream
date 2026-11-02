## Description:

Generates a new video whose speaker's lip movements match supplied audio using dLazy's hosted sync-lipsync v3 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use it to dub or localize videos and re-sync virtual presenters by pairing a video with audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video, audio, and prompts are sent to dLazy's hosted service for processing.

Mitigation: Submit only media and prompts you are comfortable sending to dLazy, and review the service terms.

Risk: The skill's example invocation and output description conflict with its lip-sync inputs and intended video result.

Mitigation: Check `dlazy sync-lipsync-3 -h` for current accepted options and confirm the returned result before relying on it.

Risk: The dLazy organization API key is stored in local CLI configuration unless supplied per invocation.

Mitigation: Protect the local configuration file and rotate or revoke the key if it is exposed.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Generated video file or hosted result URL, plus command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Takes video and audio inputs with a selectable synchronization mode; requires a dLazy API key.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
