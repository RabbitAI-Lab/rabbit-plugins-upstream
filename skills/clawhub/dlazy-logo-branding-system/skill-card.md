## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, brand teams, and agents use this skill to plan a stepwise logo and brand identity workflow, generate core mark concepts with dLazy, and extend confirmed marks into variants and branded applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on the third-party dLazy CLI and API, including npm installation and authenticated SaaS calls.

Mitigation: Verify the @dlazy/cli package before installation and use the pinned global install command or npx command only after review.

Risk: Prompts and local media files provided to the CLI may be uploaded to dLazy services for generation.

Mitigation: Provide only media files intended for upload and avoid sensitive assets unless they are approved for that service.

Risk: Manual API-key handling can expose credentials.

Mitigation: Use the dlazy login device-code flow when possible, and rotate or revoke API keys from the dLazy dashboard if exposed.

Risk: The security guidance notes a version mismatch that may affect strict supply-chain assurance.

Mitigation: Review release metadata and CLI package version alignment before regulated or high-assurance deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with requirements summaries, concept rationales, phase plans, confirmation prompts, todo status, and single-command dLazy CLI invocations when generation is confirmed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs returned by dLazy-hosted files after CLI execution.]

## Skill Version(s):

1.2.12 (source: server release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
