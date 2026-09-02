## Description:

A complete workflow skill for marketing brochure design, covering requirements gathering, layout design, and mock-up delivery through a layout-first workflow with a mandatory confirmation gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and design-support agents use this skill to plan brochure content, generate unfolded layouts, and produce folded and lifestyle mock-ups after explicit layout approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brochure prompts and approved reference media may be sent to dLazy cloud endpoints.

Mitigation: Use the skill only when dLazy cloud processing is acceptable for the project data, and avoid sensitive material unless approved for that service.

Risk: The workflow requires a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Handle the API key under local secret-management practices, and rotate or revoke keys when they are no longer needed.

Risk: Global CLI installation may be unsuitable for environments with stricter package review requirements.

Mitigation: Review the package or source before global installation, or use the documented npx command for on-demand execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI source and homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dLazy cloud APIs; generated layouts and mock-ups depend on user confirmation and supplied references.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
