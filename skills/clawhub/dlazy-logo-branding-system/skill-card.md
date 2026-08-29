## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan, generate, and iterate logo concepts, mark variants, brand applications, and identity-system deliverables through a staged dLazy CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media can be sent to dLazy services.

Mitigation: Avoid uploading confidential brand assets unless dLazy cloud processing matches the user's data policy.

Risk: The dLazy login flow can store an API key in ~/.dlazy/config.json.

Mitigation: Use DLAZY_API_KEY for per-session credentials when local key storage is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: Artifact prose contains a stale CLI version reference.

Mitigation: Use the metadata install target @dlazy/cli@1.2.3 and verify the installed CLI version before use.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with staged plans, confirmation prompts, inline shell commands, and generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication and uses one confirmed generation command at a time.]

## Skill Version(s):

1.2.7 (source: server release evidence; artifact frontmatter is 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
