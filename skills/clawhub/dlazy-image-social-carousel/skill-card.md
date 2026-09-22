## Description:

A structured workflow skill dedicated to social-media carousel design using a single-confirmation, cover-first process.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to plan and generate social-media carousel image sets with a confirmed direction, approved cover, and visually consistent follow-on slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, generation parameters, and selected media to dLazy cloud endpoints.

Mitigation: Use only prompts and media intended for dLazy, avoid private media unless intended, and review the CLI package and source before installation.

Risk: The workflow requires a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Protect the API key, prefer scoped operational use, and rotate or revoke the key when access is no longer needed.

Risk: A global CLI install requires trusting the @dlazy/cli package on the local system.

Mitigation: Prefer npx for temporary use when a global install is not needed, and install only after reviewing the package/source.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with confirmation tables, concise guidance, inline shell commands, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a cover-first workflow: confirm direction, generate the cover, then generate remaining slides to match the approved cover.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
