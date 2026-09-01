## Description:

LinkPix helps agents analyze short-video links, extract reusable script structure, generate adapted marketing videos with qhkit, and extract audio from resolved video URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to reverse-engineer viral short-video structure from Douyin or TikTok-style links, adapt the script for a user's own product, generate similar marketing video content, or extract audio/BGM from a resolved video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt users to share an API key directly in chat.

Mitigation: Use a local secure credential flow instead: configure QHKIT_TOKEN or qhkit config locally, and have the agent verify only that configuration is present.

Risk: Video generation actions can consume credits and create tasks.

Mitigation: Review the model, duration, inputs, and estimated credit cost before approving any generate action.

Risk: Replicating viral videos or extracting BGM can create copyright or misuse concerns.

Mitigation: Adapt scripts to the user's own product and obtain rights for audio or source material before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-toolkit)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQingHu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with qhkit and ffmpeg command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide the agent to produce video task submissions, status checks, generated video URLs, extracted audio files, and credit estimates.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
