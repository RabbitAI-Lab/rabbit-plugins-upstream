## Description:

Qinghu AI Viral Video Imitation for women's fashion helps an agent use a reference video and model image to transfer motion onto a new real or virtual model for short apparel promotion videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create women's apparel promotional videos by estimating cost, submitting a Qinghu workflow job through QHKit, polling until completion, and returning generated media links. It is intended for owned or authorized reference videos and model images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media is sent to Qinghu for processing.

Mitigation: Use only media the user owns or is authorized to process, and confirm they are comfortable sending it to Qinghu before generation.

Risk: Generation can spend Qinghu credits after the estimate step.

Mitigation: Run the QHKit estimate with the same parameters as generation, disclose the credit estimate, and wait for user confirmation before submitting.

Risk: The workflow depends on a local QHKit installation and a Qinghu API token.

Mitigation: Prefer a pinned or isolated QHKit installation and use existing secure token configuration or environment variables rather than exposing credentials in prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-womens)
- [QHKit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses QHKit workflow commands; final agent responses may include generated video or file URLs and actual Qinghu credit consumption.]

## Skill Version(s):

0.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
