## Description:

基于一个印花快速生成多个 POD 设计变体，支持不同配色、风格和元素组合，以提高图案量产效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External POD and ecommerce design users can use this skill to guide an agent through creating multiple print pattern variations from a reference image, including color, theme, element, and layout changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to install or upgrade qhkit or Node tooling on the host.

Mitigation: Review setup commands before execution and prefer running the skill in an isolated environment.

Risk: The skill may reuse an existing root-owned qhkit service token when present.

Mitigation: Provide a scoped qhkit token through an environment variable when possible and avoid sharing broad host credentials.

Risk: Generated pattern variants can alter important print details.

Mitigation: Review generated images for key motif, color, and layout fidelity before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-variations)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / iqinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit/Node tooling and qhkit authentication; generated images should be reviewed for pattern fidelity before production use.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
