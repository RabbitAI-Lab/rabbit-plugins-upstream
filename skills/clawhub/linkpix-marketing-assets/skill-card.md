## Description:

LinkPix routes e-commerce marketing requests to qhkit image and video workflows for product images, scene images, detail pages, promotional posters, ad images, and ad videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and agent operators use this skill to plan and generate e-commerce marketing asset bundles through qhkit. The workflow covers mixed image and video deliverables, estimates credit use where supported, and requires approval before credit-spending generation calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Environment bootstrap instructions may install global Node/npm tooling or fetch Node binaries from a registry mirror.

Mitigation: Review installation commands before execution and prefer an already provisioned Node/qhkit environment or user-scoped install path when global installation is not acceptable.

Risk: The skill may reuse an existing qhkit/OpenClaw token profile when present.

Mitigation: Confirm which token profile or QHKIT_TOKEN will be used before running qhkit commands, especially in shared environments.

Risk: Generation calls can spend credits.

Mitigation: Run estimate where supported and require explicit user approval of model, asset count, reference images, dimensions, and estimated credits before generate.

## Reference(s):

- [ClawHub skill release: linkpix-marketing-assets](https://clawhub.ai/autoagc/skills/linkpix-marketing-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit qhkit image or video generation tasks after estimate review and explicit user confirmation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
