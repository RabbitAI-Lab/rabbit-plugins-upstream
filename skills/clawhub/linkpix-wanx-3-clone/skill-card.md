## Description:

Helps e-commerce video teams analyze a reference clip, adapt its script for their product, and create a short video using a selected Wanx model through qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce video teams and merchants use the skill to adapt the pacing and selling points of reference videos for their own products and generate short promotional videos for Taobao-related channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to paste a long-lived API key into chat.

Mitigation: Configure QHKIT_TOKEN through a secret store or environment variable outside the conversation.

Risk: The skill installs or updates mutable Node/npm command-line dependencies.

Mitigation: Review qhkit and the required Node/npm installation before running the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-wanx-3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Video links]

**Output Format:** [Markdown with a script comparison and a link to the generated video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation consumes credits and requires user confirmation before submission.]

## Skill Version(s):

0.1.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
