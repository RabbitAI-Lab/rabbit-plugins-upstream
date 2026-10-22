## Description:

ElevenLabs music_v1 model — generates 10–300s original music from a natural-language prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate original music from natural-language prompts for background music, advertisements, and short-video soundtracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy services, and generation may consume paid credits.

Mitigation: Avoid confidential inputs; use dry-run to inspect the payload and estimated cost before generating.

Risk: Logging in stores the organization API key in the local dLazy configuration.

Mitigation: Use the documented DLAZY_API_KEY environment-variable option instead of saving the key, or protect the local config and rotate or revoke the key when needed.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [Generated music audio asset with JSON result metadata and a hosted URL; optionally saved to a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates 10–300 seconds of music; asynchronous requests can return a task ID before the result is ready.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
