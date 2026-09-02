## Description:

This paid ClawHub skill helps an agent generate images from a user prompt through Juhe's AI image service and Alipay payment confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to request paid AI-generated images from prompt text, with size selection and Alipay-based payment confirmation before fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The user's image prompt is sent to Juhe, and the workflow uses a paid Alipay payment step.

Mitigation: Confirm price and payment intent before requesting the service, and avoid placing personal or sensitive information in prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-ai-image-generate-a2a)
- [Juhe A2A image generation endpoint](https://apis.juhe.cn/a2a/query)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request payloads and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts are sent to Juhe for image generation; payment is handled through Alipay skills after user confirmation.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
