## Description:

Use when someone wants one short video clip from text or images - B-roll, start/end frame animation, or a quick motion shot; not for full multi-scene films or lip-synced hosts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through creating one short Pruna p-video clip from a prompt, optional image anchors, and optional audio. It helps collect inputs, craft a faithful video prompt, and prepare the Pruna API request while redirecting multi-scene, lip-sync, and editing requests to other skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated-video requests may upload user prompts, images, and audio to Pruna.

Mitigation: Avoid private or sensitive media unless the user is comfortable sending it to Pruna, and confirm consent before submitting prompts or files.

Risk: The skill may ask the agent to install additional Pruna helper skills from a live remote repository.

Mitigation: Prefer pinned or reviewed dependency versions in stricter environments before installing helper skills.

## Reference(s):

- [p-video Skill Page](https://clawhub.ai/pruna-ai/skills/p-video)
- [Pruna Files API](https://api.pruna.ai/v1/files)
- [Pruna Predictions API](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline curl examples and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide upload, prediction creation, polling, and download steps for a single short video generation request.]

## Skill Version(s):

1.0.11 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
