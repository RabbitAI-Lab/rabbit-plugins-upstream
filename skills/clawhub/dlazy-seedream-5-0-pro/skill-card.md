## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition, suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Seedream 5.0 Pro cloud image-generation service for commercial key visuals, brand assets, and other prompt-driven image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, generation parameters, and explicitly provided media files to dLazy's hosted service.

Mitigation: Use the skill only with content appropriate for a third-party cloud service and review dLazy's service terms before sending sensitive material.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Protect the saved API key like other credentials, prefer npx for non-persistent use when appropriate, and rotate or revoke the key if it may have been exposed.

Risk: Installing the global CLI persists a third-party package on the system.

Mitigation: Prefer the pinned npx invocation for occasional use, or review the referenced package and source links before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs and optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers when run with no-wait mode; generated assets are hosted by files.dlazy.com.]

## Skill Version(s):

1.2.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
