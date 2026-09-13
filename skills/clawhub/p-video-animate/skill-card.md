## Description:

Use when someone wants a photo to move like another video -- motion transfer, dance remixes, or performance variations from a template clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to animate a still reference image with motion copied from a source video through Pruna's p-video-animate model. It guides input collection, prompt discipline, API submission, polling, and follow-on editing choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user media and prompts to a third-party Pruna API.

Mitigation: Use only media and likenesses that the user is authorized to process, and review Pruna handling and retention terms before using sensitive or private assets.

Risk: The skill recommends remote npx skill installation commands that may change over time.

Mitigation: Review and pin dependency installation commands before execution in controlled environments.

Risk: The optional disable_safety_checker setting could weaken model safety controls.

Mitigation: Leave safety checks enabled unless there is a documented, policy-compliant reason to disable them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-animate)
- [Pruna AI publisher profile](https://clawhub.ai/user/pruna-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image and video asset upload, asynchronous prediction creation, polling, download, and optional prompt and generation settings.]

## Skill Version(s):

1.0.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
