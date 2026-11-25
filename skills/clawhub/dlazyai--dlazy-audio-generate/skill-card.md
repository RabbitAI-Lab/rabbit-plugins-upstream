## Description:

Audio generation skill. Automatically selects the best dlazy CLI audio/TTS model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can use the skill to generate speech, music, dialogue, and sound effects, or search for voices, by having an agent select and run a suitable dLazy CLI model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied to generation commands may be sent to dLazy-hosted services for processing and storage.

Mitigation: Review the service's data handling terms and avoid sending sensitive prompts or files unless that use is authorized.

Risk: The security evidence reports partial scanner coverage and documentation issues, and notes capabilities beyond the stated audio purpose.

Mitigation: Review the documented model, command, and service behavior before execution, especially when a request involves media beyond audio.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy service](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project link declared in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON, Guidance]

**Output Format:** [Generated audio and hosted output URLs, with CLI results returned in a JSON envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Prompts and supplied media may be sent to dLazy-hosted services.]

## Skill Version(s):

1.3.48 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
