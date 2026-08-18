## Description:

This skill helps agents plan and run AI Hive Seedance 2.5 video generation and editing workflows as a Pika alternative for single-effect short videos, including text-to-video, image animation, reference-timed generation, video editing, and extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to translate Pika-style short video ideas into controlled AI Hive Seedance 2.5 generation and editing runs. It is intended for single-effect product, social, object-transformation, and vertical video workflows where prompts must preserve approved subjects and avoid copying Pika proprietary templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected images or videos are uploaded to AI Hive during generation or editing workflows.

Mitigation: Use only media that the user has rights to upload and confirm that the selected files are appropriate for AI Hive processing before running the CLI.

Risk: An AI Hive API key may be stored locally or provided through the environment.

Mitigation: Use an API key the user is comfortable using for AI Hive, keep local configuration permissions restricted, and rotate the key if it is exposed.

Risk: Generated video files are downloaded to the local machine.

Mitigation: Review downloaded outputs before reuse or publication and store them according to the user's media handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/pika-video-generation-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline bash commands and Python CLI configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can submit AI Hive video generation tasks, upload user-selected media, poll task status, and download generated MP4 files when the CLI is executed.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
