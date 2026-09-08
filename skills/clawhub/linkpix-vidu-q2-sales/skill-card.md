## Description:

Helps e-commerce merchants, designers, and storefront operators use Qinghu qhkit with Vidu Q2 to generate product sales videos from product images, selling points, and model options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce creators and operators use this skill to prepare, estimate, submit, and monitor Vidu Q2 product video generation through qhkit. It is aimed at product demos, marketplace listings, social ads, and material-consistent showcase clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask users to expose an API key in chat.

Mitigation: Use a secret manager, masked credential prompt, or QHKIT_TOKEN environment variable instead of pasting raw API keys into chat.

Risk: The skill directs agents to install or run mutable third-party packages with broad local effects.

Mitigation: Review installation commands, prefer a dedicated or sandboxed environment, and pin package versions instead of automatically upgrading to latest.

Risk: Uploaded product media and prompts may be sent to the Qinghu/qhkit service and video generation may consume credits.

Mitigation: Confirm media handling and costs before generate actions, and use available estimate commands before submitting tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-vidu-q2-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide qhkit CLI use for product media upload, credit estimation, video task submission, status polling, and delivery of generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
