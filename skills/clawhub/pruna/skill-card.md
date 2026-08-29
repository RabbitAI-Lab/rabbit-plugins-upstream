## Description:

Use when installing the full Pruna generative media suite: guides, tools, and workflows in one package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to install and navigate the Pruna generative media suite for image, video, audio, and multi-step media workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suite may use API credentials and make paid external API calls.

Mitigation: Confirm the user intends to use Pruna or Replicate services and has approved any paid calls before execution.

Risk: Media, prompts, or related content may be uploaded to Pruna and sometimes Replicate.

Mitigation: Avoid submitting sensitive content unless the user is comfortable with those services handling it.

Risk: Local media tools such as curl, ffmpeg, and ffprobe may process downloaded or generated assets.

Mitigation: Review proposed shell commands and file paths before running media processing steps.

## Reference(s):

- [Pruna Skill on ClawHub](https://clawhub.ai/pruna-ai/skills/pruna)
- [Pruna Dashboard](https://dashboard.pruna.ai/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to use API credentials, paid external API calls, media uploads, and local media tools such as curl, ffmpeg, and ffprobe.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
