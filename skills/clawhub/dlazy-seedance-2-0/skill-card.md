## Description:

Guides agents through text-to-video and reference-guided video generation with Seedance 2.0 using dLazy's cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate videos from text prompts, media references, or first and last frames through a dLazy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external CLI requires a paid dLazy account and may incur usage charges.

Mitigation: Review account costs and use a dry run to estimate charges before generation.

Risk: Selected local images, videos, or audio are uploaded to dLazy for generation.

Mitigation: Only provide media you intend to share with dLazy.

Risk: Login saves an API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials if preferred; review or revoke stored keys in the dLazy dashboard.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through hosted URLs; the CLI can save results locally.]

## Skill Version(s):

1.3.26 (source: server release metadata; skill frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
