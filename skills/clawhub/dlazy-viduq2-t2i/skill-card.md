## Description:

Generate high-quality images with Vidu Q2 from text prompts or image inputs through the dLazy hosted CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to invoke dLazy's Vidu Q2 text-to-image and image-to-image workflow, passing prompts, optional image inputs, aspect ratio, resolution, and save or async options. It is intended for users who are comfortable authenticating to dLazy and using a hosted image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image inputs may be uploaded to dLazy's hosted API and media storage.

Mitigation: Avoid sending confidential or regulated content unless the user has approved dLazy as an external service for that data.

Risk: The CLI can store a dLazy API key in a local user configuration file.

Mitigation: Use least-privilege API keys where possible, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables or npx when avoiding persistent setup.

Risk: API calls may consume account credits and can fail when the account has insufficient balance.

Mitigation: Use dry-run or cost-estimate behavior before expensive runs when available, and surface insufficient-balance errors clearly to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted CLI returns image output URLs, MIME type metadata, or async task status; users may optionally save generated assets locally.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
