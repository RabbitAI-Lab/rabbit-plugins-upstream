## Description:

This skill helps cross-border sellers, MCN teams, and ad operators generate TikTok commerce videos with LinkPix/qhkit, including multilingual talking-head clips, short skits, product seeding videos, and vertical ad-ready videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, MCN teams, and ad operators use this skill to prepare and submit TikTok Shop or TikTok Ads video-generation tasks, check estimates and task status, and retrieve generated video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade local Node tooling before use.

Mitigation: Review the package source and installation command, and run it only in an environment where qhkit and Node package changes are acceptable.

Risk: The skill workflow may request a persistent API key.

Mitigation: Provide credentials through a local secret mechanism or environment variable rather than pasting keys into chat.

Risk: Generation commands can consume credits and upload local media files.

Mitigation: Confirm the selected model, duration, uploaded files, and estimated credits before running any generate command.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-tiktok-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce video task IDs, status guidance, cost-estimate guidance, and generated video URLs when the user authorizes a generation task.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
