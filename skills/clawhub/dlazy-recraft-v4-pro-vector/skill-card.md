## Description:

High-fidelity text-to-vector model with 4MP-tier quality for producing production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill through the dLazy CLI to generate vector-style image assets from prompts and optionally save the generated result to a local file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a third-party hosted generation service through the dLazy CLI.

Mitigation: Install only if you trust dLazy and the pinned @dlazy/cli package.

Risk: Authentication uses a dLazy API key.

Mitigation: Use a revocable API key and rotate or revoke it from the dLazy dashboard when access is no longer needed.

Risk: Local files passed to media parameters may be uploaded to the hosted service.

Mitigation: Pass only files intended for upload and avoid sensitive inputs unless approved for the service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration]

**Output Format:** [JSON responses with generated asset URLs, plus optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and uses the pinned @dlazy/cli package version declared in the skill metadata.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
