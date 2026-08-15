## Description:

A workflow skill for planning marketing brochure content, generating brochure layouts, confirming the layout with the user, and producing folded and lifestyle mock-ups through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to plan brochure structure, generate layout-first brochure artwork, and create folded or lifestyle mock-ups after explicit layout approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brochure prompts and uploaded reference images are processed through dLazy cloud services.

Mitigation: Avoid sending confidential media unless appropriate for the intended use, and use the skill only when cloud processing is acceptable.

Risk: The workflow depends on a third-party CLI and API key.

Mitigation: Review the pinned CLI package if needed, prefer npx to avoid a persistent global install, and rotate or revoke the dLazy API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI authentication and sends prompts plus referenced media to dLazy cloud services.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
