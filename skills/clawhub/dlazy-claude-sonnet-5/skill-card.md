## Description:

Uses the dLazy CLI to generate text, code, and reasoning responses from prompts with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users invoke the dLazy CLI to obtain model-generated answers, code, and guidance from text prompts and optional media inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to the dLazy service.

Mitigation: Do not submit sensitive prompts or files unless you intend to share them with dLazy.

Risk: The CLI requires an API key and can store it in local configuration.

Mitigation: Trust the CLI and service before installing; use DLAZY_API_KEY for per-invocation credentials when local persistence is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON response containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before generated content is available.]

## Skill Version(s):

1.2.32 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
