## Description:

Guides agents through staged logo design and development of a consistent brand visual system, from core mark to applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, brand teams, and other agents use this skill to plan logo concepts, obtain approval, and develop consistent variants and brand applications with dLazy image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's cloud service for generation.

Mitigation: Use the service only when this data transfer is acceptable; do not upload sensitive media unless intended.

Risk: Installing the third-party CLI introduces a software supply-chain dependency.

Mitigation: Review the @dlazy/cli package source when assurance matters and confirm the installed version is 1.2.3.

Risk: A version typo in the skill documentation could cause installation confusion.

Mitigation: Check the installation command and confirm the intended CLI version before running it.

Risk: The dLazy API key grants access to the user's dLazy organization.

Mitigation: Keep the key private and rotate or revoke it in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI repository (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with design concepts, brand-system guidance, and CLI commands; generated image URLs when used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Staged deliverables and confirmation between design phases]

## Skill Version(s):

1.2.19 (source: ClawHub release metadata; bundled skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
