## Description:

High-fidelity text-to-vector model for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and external users use this skill to invoke dLazy's hosted Recraft V4 Pro Vector generation CLI and produce vector-style image assets from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any referenced local media are sent to dLazy's hosted API and media storage for processing.

Mitigation: Avoid passing private files unless upload to dLazy is intended, and review the service terms before use.

Risk: The skill depends on dLazy's npm CLI and a dLazy API key.

Mitigation: Confirm the CLI and service are trusted before installing, prefer npx or DLAZY_API_KEY when avoiding global installation or persistent credentials, and rotate or revoke keys when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI Repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as hosted file URLs, with optional local save paths handled by the dLazy CLI.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
