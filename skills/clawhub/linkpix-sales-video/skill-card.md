## Description:

Generates short product-promotion videos from product images and selling points, with scripts, narration, subtitles, and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Online sellers and marketing teams use this skill to turn product images and selling points into short promotional videos for platforms such as TikTok and Douyin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update software and change the local Node/npm environment.

Mitigation: Review the environment impact and confirm package installation or PATH changes before execution.

Risk: Product images or video may be uploaded to LinkPix/qhkit, and the workflow uses an API token.

Mitigation: Use only approved media in an intended workspace and supply the token through a secure secret mechanism.

Risk: Video generation can consume paid credits.

Mitigation: Confirm the generation task and expected charges before submitting it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-sales-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with video links and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes generation status and credit charges when available.]

## Skill Version(s):

0.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
