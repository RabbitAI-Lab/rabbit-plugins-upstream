## Description:

Helps Xiaohongshu creators and merchants generate product-promotion videos from prompts and media using the qhkit service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Xiaohongshu creators, buyers, and merchants use this skill to plan and generate short product-demonstration, unboxing, and lifestyle videos for posts and promotions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for an API key and may store it through qhkit; sharing it in chat can expose the credential.

Mitigation: Set the token yourself through a local environment variable or secure secret mechanism, review where qhkit stores credentials, and rotate any key pasted into chat.

Risk: Installing or upgrading the npm package may introduce changes to tooling in the user's environment.

Mitigation: Review and approve the package installation and its version before running it.

Risk: Media supplied for video generation is uploaded to the qhkit service, and generation consumes credits.

Mitigation: Upload only media you are comfortable sharing and confirm the model, inputs, and expected credit cost before submitting a task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-xiaohongshu-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [qhkit API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Video links]

**Output Format:** [Markdown with commands and links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task status and credits used; video generation requires user confirmation before submission.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
