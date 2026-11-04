## Description:

Convert static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn reference images or supplied first and last frames into Vidu Q2 generated videos through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external dLazy CLI means trusting code that was not audited for this release.

Mitigation: Review the CLI project before installing and use the documented pinned @dlazy/cli version.

Risk: Prompts and selected media are sent to dLazy, and generation may consume credits.

Mitigation: Upload only media approved for the service, and review its privacy terms and pricing before generating.

Risk: The CLI stores an API key in the user's local configuration.

Mitigation: Protect the local configuration and rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI project (metadata link)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)
- [dLazy credits settings](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Generated video asset or JSON result containing media URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation options include prompt, image or frame inputs, duration, aspect ratio, resolution, and optional audio; completed media is hosted by dLazy.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
