## Description:

Generates ecommerce video ad assets from product information for feed ads, brand promotion, and social media marketing, including batch production through LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce marketers, agency operators, and agent users use this skill to prepare batches of short video ad assets for social feeds, brand promotion, and platform-specific campaigns. The skill guides model selection, price estimation, task submission, polling, and final video URL delivery through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update qhkit and related media tooling, including possible PATH or shell profile changes.

Mitigation: Review install and upgrade commands before making changes persistent, and prefer the existing qhkit installation when it is already configured.

Risk: The skill requires a LinkPix/qhkit API token and may guide users through local credential configuration.

Mitigation: Enter secrets through a trusted local config flow or environment variable, avoid sharing tokens in chat history when possible, and verify that displayed config output is masked.

Risk: Product images selected for generation may be uploaded to the LinkPix/qhkit service.

Mitigation: Use only approved images and URLs for the campaign, and confirm which reference images will be uploaded before task submission.

Risk: Video generation can spend credits and submitted tasks may not be cancelable.

Mitigation: Run price estimation when supported, summarize model, count, orientation, language, reference images, and expected credits, and wait for explicit user confirmation before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-ad-assets)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with qhkit JSON command examples, confirmation text, task status, and delivery URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate paid video generation only after price estimation and explicit user approval; generated task IDs, status, video URLs, and credit usage are returned when available.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
