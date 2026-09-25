## Description:

Guides an agent through using Grok Imagine to generate images from user prompts, save generated images locally, and optionally send them through Feishu.

This skill is ready for commercial/non-commercial use.

## Publisher:

[279458179](https://clawhub.ai/user/279458179)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users use this skill when they need Grok Imagine to create an image from a text prompt, then save or share the result. It is useful for image-generation workflows that rely on browser interaction and local file handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to Grok Imagine, so user-provided image descriptions may leave the local agent environment.

Mitigation: Ask for explicit user approval before submitting prompts and avoid sending sensitive or confidential details.

Risk: The workflow uses unpinned desktop automation and browser interactions that can change when the page or desktop state changes.

Mitigation: Prefer a reviewed and pinned automation tool or safer browser download path, and verify page state before acting.

Risk: Generated images may be saved locally or sent through Feishu without clear consent boundaries.

Mitigation: Require explicit user approval before saving files or sending images, and confirm the destination path or recipient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/279458179/skills/grok-image-generate)
- [Publisher profile](https://clawhub.ai/user/279458179)
- [Grok Imagine](https://grok.com/imagine)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JavaScript and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local image files when the user approves saving generated images.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
