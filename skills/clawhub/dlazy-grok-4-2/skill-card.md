## Description:

Generates text, answers questions, and supports reasoning using the Grok 4.2 model through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users can generate text, answer questions, and work through reasoning tasks using the dLazy-hosted Grok 4.2 model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any user-specified media may be sent to dLazy's cloud service, where generated files may also be hosted.

Mitigation: Invoke deliberately and avoid submitting sensitive prompts or files without authorization.

Risk: The dLazy login stores an API key in local CLI configuration.

Mitigation: Protect the local key and rotate or revoke it in the dLazy dashboard when access is no longer needed.

Risk: Using the skill installs or runs a third-party npm CLI.

Mitigation: Review the pinned CLI package and source before installation if required by your security policy.

## Reference(s):

- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Text in a JSON CLI response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID instead of generated text.]

## Skill Version(s):

1.3.21 (source: ClawHub release record)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
