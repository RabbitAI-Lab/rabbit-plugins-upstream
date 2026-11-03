## Description:

Creates a single ElevenLabs eleven_v3 dialogue audio track from up to 20 lines, with up to 10 distinct voices and expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and agents can turn scripted multi-speaker dialogue into a generated voice track for character scenes, podcasts, or short skits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text and any selected media are sent to dLazy services for processing.

Mitigation: Avoid sending confidential or sensitive content unless you accept that transfer and the service terms.

Risk: The workflow uses an API key and may spend service credits; the external CLI distribution and credential-file protections were not independently verified.

Mitigation: Prefer device-code login, keep API keys out of chat, and use --dry-run to review inputs and estimated cost before generating.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, API results]

**Output Format:** [Generated audio asset or hosted audio URL, with JSON status for asynchronous jobs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dialogue can contain up to 20 lines and use up to 10 distinct voices.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
