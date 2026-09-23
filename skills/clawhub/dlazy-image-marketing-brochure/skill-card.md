## Description:

A workflow skill for designing marketing brochures from requirements gathering through layout generation, approval, folded mock-ups, and lifestyle mock-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to plan brochure structure, generate brochure layouts, and produce folded and lifestyle mock-ups after explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brochure prompts, brand materials, and referenced media may be sent to dLazy cloud services.

Mitigation: Use the skill only when that sharing is acceptable, and avoid uploading confidential or unreleased assets unless approved.

Risk: The workflow depends on a third-party CLI, local API-key configuration, network calls, and media uploads.

Mitigation: Prefer npx for non-persistent use, review the package or source before installation, and rotate or revoke the dLazy API key if the local config is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user confirmation gates before generation and before moving from approved layouts to mock-ups.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
