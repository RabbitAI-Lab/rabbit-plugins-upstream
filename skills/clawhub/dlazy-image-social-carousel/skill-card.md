## Description:

A structured workflow skill dedicated to social-media carousel design using a single-confirmation, cover-first flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and agent operators use this skill to plan and generate social-media carousel image sets with a confirmed direction, approved cover, and consistent remaining slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be sent to dLazy's hosted service.

Mitigation: Use the skill only when cloud processing by dLazy is acceptable for the project data.

Risk: Using dlazy login or dlazy auth set can store an API key in the local CLI configuration.

Mitigation: Prefer environment-scoped credentials where appropriate and rotate or revoke dLazy API keys from the dLazy dashboard when access changes.

Risk: The workflow depends on the documented dLazy CLI package version.

Mitigation: Review the dLazy CLI source or npm package before installing when dependency provenance matters to the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown status updates, confirmation tables, prompt drafts, CLI commands, and generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a staged workflow with user confirmation before image generation and before continuing from the approved cover to remaining slides.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
