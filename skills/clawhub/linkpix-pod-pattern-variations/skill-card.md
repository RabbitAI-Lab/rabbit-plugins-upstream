## Description:

This skill helps agents generate multiple POD print design variations from a reference pattern using the qhkit CLI, varying colors, styles, elements, and layout density.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn a single POD print or pattern into a family of related design variants for ecommerce SKU expansion. It is suited for colorway, theme, element-combination, and layout-density variation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a local qhkit token or account and may consume image-generation credits.

Mitigation: Confirm the intended qhkit account and token before generation, and use qhkit image estimate before reporting or committing to credit usage.

Risk: The skill includes host-level Node/npm installation and upgrade steps for qhkit.

Mitigation: Review installation commands before execution and avoid automatic global npm or Node changes unless the user explicitly wants those host changes.

Risk: Generated print variations can differ from the source pattern in small details.

Mitigation: Review generated outputs for key motif, color, and layout fidelity before using them in POD production.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-variations)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and actual credit usage when qhkit image generation succeeds.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
