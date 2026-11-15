## Description:

Creates an ElevenLabs eleven_v3 multi-voice dialogue by assigning voices to lines and rendering the conversation in one generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, podcasters, and developers can turn a scripted conversation into a multi-voice dialogue, assigning voices to individual lines and adding expressive audio tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags login and authentication commands as not clearly aligned with the described dialogue task.

Mitigation: Review the CLI login and API-key steps and decide whether they fit the intended workflow before installing or running the skill.

Risk: The scan is incomplete because several local references were unresolved.

Mitigation: Resolve and review those references before relying on behavior they may define.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio asset (download URL or saved audio file), with JSON task status and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 20 dialogue lines and 10 unique voices per generation; asynchronous tasks can return a task identifier and status.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
