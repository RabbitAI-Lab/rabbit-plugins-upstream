## Description:

Alibaba's Qwen reasoning model skill accepts text and image input for complex reasoning, code engineering, and long-context analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users submit text prompts, optionally with images, to generate content with Qwen 3.8 Max for reasoning, coding, and long-context analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy for inference, and requests may consume credits.

Mitigation: Avoid submitting sensitive inputs, review expected usage costs, and use --dry-run to inspect the payload and cost estimate before calling the API.

Risk: Logging in stores the organization API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable when you prefer not to save the key locally, and rotate or revoke exposed keys.

Risk: Installing the pinned third-party CLI package introduces a software supply-chain dependency.

Mitigation: Review the pinned CLI package and its project information before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response envelope containing model-generated output; asynchronous requests may return a task identifier.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts text prompts and up to 10 images; completed generated assets may be saved locally.]

## Skill Version(s):

1.2.29 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
