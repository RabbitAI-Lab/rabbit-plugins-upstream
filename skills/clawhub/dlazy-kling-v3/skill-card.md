## Description:

Generates high-quality videos from text prompts or image inputs with Kling v3 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to ask an agent to generate Kling v3 videos from text prompts or from up to two image inputs, with options for aspect ratio, duration, mode, sound, async polling, and local saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media can be uploaded to dLazy's hosted service.

Mitigation: Use the skill only with content suitable for upload to dLazy, and avoid providing confidential or restricted media unless that use is approved.

Risk: The dLazy API key is stored locally or supplied through the DLAZY_API_KEY environment variable.

Mitigation: Protect local configuration and environment variables, and rotate or revoke the API key from dLazy if exposure is suspected.

Risk: Generated outputs are hosted remotely and API usage may consume credits.

Mitigation: Review generated output URLs before sharing, use dry-run or async controls where appropriate, and monitor account balance before running large jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON responses containing hosted output URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are hosted remotely; async runs may return a generateId for polling, and --save can download the generated asset locally.]

## Skill Version(s):

1.3.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
