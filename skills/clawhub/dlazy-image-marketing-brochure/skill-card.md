## Description:

Marketing Brochure guides agents through requirements gathering, layout-first brochure design, explicit user confirmation, and mock-up generation for marketing brochure workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and marketing teams use this skill to plan brochure content, generate layout-first brochure artwork, confirm the layout, and then produce folded and lifestyle mock-ups through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI and cloud API that can receive prompts, API keys, and local media inputs.

Mitigation: Review the @dlazy/cli package or source before installation and only provide API keys or media that are acceptable to send to dLazy's hosted service.

Risk: The security guidance notes a documentation mismatch between CLI versions 1.2.3 and 1.0.9.

Mitigation: Confirm the intended @dlazy/cli version before installation, and prefer npx or an isolated environment when avoiding a persistent global install.

Risk: Stored dLazy API keys may remain usable after the workflow is complete.

Mitigation: Use environment-scoped credentials when possible and rotate or revoke the API key after use if it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a layout-first confirmation gate before folded and lifestyle mock-up generation.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
