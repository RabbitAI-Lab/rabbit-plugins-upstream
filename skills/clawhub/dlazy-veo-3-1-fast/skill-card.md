## Description:

Generates short text-to-video or image-to-video clips with Veo 3.1 Fast through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts or reference images, including video extensions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached media are sent to a third-party cloud service, and generated videos are hosted there.

Mitigation: Avoid sensitive inputs unless dLazy's data handling and hosting terms meet your needs.

Risk: Login stores a service API key locally.

Mitigation: Protect the local key or use the environment-variable option; rotate or revoke compromised keys.

Risk: The documented video examples use a flag that does not appear in the option list.

Mitigation: Check the CLI help for supported flags before running generation.

Risk: Installation relies on a third-party npm CLI.

Mitigation: Review the pinned CLI package and its source before installation if supply-chain trust matters.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Text guidance and commands; CLI returns JSON with generated media URLs or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video is hosted by dLazy; the CLI can download it to a local path.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
