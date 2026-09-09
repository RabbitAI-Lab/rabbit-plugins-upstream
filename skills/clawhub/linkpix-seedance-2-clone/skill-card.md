## Description:

Guides agents through LinkPix/Qinghu workflows for analyzing short-form video references, rewriting them for a user's product, and generating Seedance 2.0 product videos through qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agent users can use this skill to transform a short-form video reference into a product-focused script and qhkit video generation workflow. It is aimed at Douyin, TikTok, Xiaohongshu, and similar social commerce video production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to install or upgrade mutable third-party command-line packages.

Mitigation: Install only in a controlled or sandboxed environment, review package sources before deployment, and prefer pinned dependency versions where operationally feasible.

Risk: The workflow uses a production Qinghu API key and may upload user-provided media to a third-party service.

Mitigation: Configure credentials through managed secrets or local environment variables, avoid pasting keys into chat, and confirm media handling expectations before uploading content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedance-2-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rewritten video scripts, qhkit command parameters, polling guidance, and final media links when generation completes.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
