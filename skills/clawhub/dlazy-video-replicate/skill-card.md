## Description:

Helps agents replicate a source video by extracting its first frame and audio, generating a descriptive prompt, and requesting a Seedance 2.0 video replication bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate a video replication bundle from a reference video using dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Confirm the user is comfortable sharing sensitive media before submitting it; review the external CLI package before installation.

Risk: A dLazy API key may be stored in local user configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY option where appropriate, and protect or rotate stored credentials.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with CLI commands and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a first frame, audio, video, or an asynchronous task ID.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
