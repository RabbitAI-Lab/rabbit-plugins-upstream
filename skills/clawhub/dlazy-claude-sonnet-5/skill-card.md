## Description:

Helps agents generate text, code, and responses to prompts through dLazy's hosted Claude Sonnet 5 service, with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users use this skill to draft text, generate code, and answer questions using text prompts or optional visual inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image or video files can be sent to dLazy's hosted service.

Mitigation: Submit only content approved for the service; check local file selections before invoking the skill.

Risk: The CLI can save an API key locally, and a global installation persists on the device.

Mitigation: Use a per-invocation API key and the documented on-demand npx option when local persistence is undesirable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [Text returned in a JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an immediate response.]

## Skill Version(s):

1.2.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
