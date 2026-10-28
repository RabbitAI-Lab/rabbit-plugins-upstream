## Description:

ElevenLabs text-to-sound model that generates 1–22 second sound effects from a description for foley, ambience, alerts, and game audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short sound effects from text prompts for foley, ambience, alerts, and game audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media files explicitly provided for generation are sent to dLazy's hosted service.

Mitigation: Only submit content you are comfortable sharing with the service, and use --dry-run to preview the request and estimated cost.

Risk: Logging in saves an API key in the local dLazy CLI configuration.

Mitigation: Prefer device-code login, protect access to the local account, and rotate or revoke the key if needed.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy CLI project link (skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [Generated sound effect with JSON result or task metadata; optionally saved to a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Short effects are 1–22 seconds; asynchronous tasks can return a task identifier before completion.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
