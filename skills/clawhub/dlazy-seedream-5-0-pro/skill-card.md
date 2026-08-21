## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition. Suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate commercial-quality Seedream 5.0 Pro images from text prompts, optional reference images, and size controls through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid-service API key may be persisted in the local dLazy configuration.

Mitigation: Prefer per-run DLAZY_API_KEY or npx usage when persistence is not needed; verify permissions on ~/.dlazy/config.json and rotate the key if exposure is suspected.

Risk: Prompts and local media paths supplied to the skill are uploaded to dLazy endpoints for cloud generation.

Mitigation: Only submit prompts and files that are acceptable to share with dLazy, and review dLazy service terms before use.

Risk: The skill uses a credit-backed service that can consume account balance.

Mitigation: Monitor credit usage and use dry-run or async options where appropriate before running expensive generations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Images, Guidance]

**Output Format:** [CLI output as JSON containing generated image URLs, with optional downloaded image files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and referenced local media are sent to dLazy endpoints for generation.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
