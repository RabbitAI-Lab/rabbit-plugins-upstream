## Description:

Guides agents through logo concepts, user-approved visual assets, and a consistent brand identity system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and brand teams use this skill to explore logo directions, confirm a core mark, and create consistent brand applications with optional cloud-generated imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media may be sent to dLazy's cloud service.

Mitigation: Avoid sharing sensitive brand materials unless the service is trusted.

Risk: The workflow installs or runs a third-party CLI and stores an API key locally.

Mitigation: Review the package before installation, use npx to avoid a global install, and rotate or revoke the key in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI source linked in skill metadata (not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown with design rationale, generation commands, and hosted image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Phase-by-phase delivery with user confirmation before generating subsequent assets.]

## Skill Version(s):

1.2.26 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
