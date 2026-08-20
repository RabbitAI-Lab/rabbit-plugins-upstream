## Description:

Generates ecommerce sales copy and video scripts from product details or comparable viral video links using LinkPix/qhkit workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to generate Chinese ecommerce sales scripts, livestream/video narration, product seeding copy, review scripts, story-driven scripts, or scripts reverse-engineered from comparable high-performing videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to install or upgrade global software using npm, curl, brew, winget, PATH changes, or similar setup commands.

Mitigation: Require explicit user approval before running installation, upgrade, PATH, or package-manager commands, and prefer the least-privileged installation path that works.

Risk: The skill may reuse an existing root-local OpenClaw token for qhkit access.

Mitigation: Use a dedicated QHKIT_TOKEN or a user-approved qhkit configuration instead of automatically reusing root-local credentials.

Risk: The skill sends product details, local media paths, or public video links to the qhkit external service for script generation.

Mitigation: Use only when the user is comfortable with that external service handling the submitted sales-script inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-sales-script)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown response containing generated script text and, when setup is needed, qhkit command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return full generated script text directly, or task status/message details from qhkit when generation or setup fails.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
