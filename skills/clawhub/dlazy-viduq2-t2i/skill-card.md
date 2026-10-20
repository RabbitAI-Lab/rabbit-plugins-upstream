## Description:

Guides an agent to generate or edit images with Vidu Q2 using text prompts and optional reference images through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents creating visual content can generate images from text or edit images using references, with optional controls for aspect ratio and resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service.

Mitigation: Confirm the user wants this provider and avoid sharing sensitive prompts or media without consent.

Risk: Authentication can store an API key in the local CLI configuration.

Mitigation: Protect the key, avoid exposing it in shared output, and rotate or revoke it if compromised.

Risk: Image generation may consume account credits.

Mitigation: Confirm the provider before generating and use the dry-run cost estimate when appropriate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with CLI commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image links or optionally saved files; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.32 (source: ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
