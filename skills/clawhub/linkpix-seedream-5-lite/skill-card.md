## Description:

Guides agents in creating Chinese-language e-commerce graphics with LinkPix image generation from prompts and optional product photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and designers use this skill to guide an agent in producing Chinese-language product images, promotional graphics, and posters from prompts or reference photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the external qhkit npm package executes third-party code.

Mitigation: Install only if the package and publisher are trusted; review or pin the package version in managed environments.

Risk: Prompts, reference images, and API credentials are used with the LinkPix service.

Mitigation: Avoid submitting sensitive images or prompts without authorization and protect the API key.

Risk: Generating images consumes service credits.

Mitigation: Estimate the cost and get the user's explicit approval of the parameters before submitting a generation request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-seedream-5-lite)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with commands and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model and credit estimates are checked before generation; successful replies include image URLs and credits used.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
