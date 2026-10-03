## Description:

Helps agents generate short videos from prompts and optional image, video, or audio references using dLazy's hosted Seedance 2.5 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts, optionally guiding the result with media references or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service.

Mitigation: Use only inputs you are comfortable sharing with the service.

Risk: Using the CLI requires an API key stored locally or supplied through an environment variable.

Mitigation: Protect the key and review the linked CLI source or package before installation if supply-chain assurance is needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON with generated-media URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally download the generated media to a local path.]

## Skill Version(s):

1.2.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
