## Description:

Image generation skill that automatically selects the best dLazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to generate, edit, upscale, vectorize, or segment images through the dLazy CLI and hosted image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a third-party npm CLI and sends prompts or referenced files to dLazy's hosted service.

Mitigation: Install only if comfortable with dLazy's cloud service, review the CLI source or package before global installation, and avoid passing sensitive local files as references.

Risk: A dLazy API key is required and may be stored in local CLI configuration.

Mitigation: Protect the API key, rotate or revoke it when needed, and use per-invocation environment variables when persistent local configuration is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through dLazy-hosted result URLs; local prompts and referenced files may be sent to dLazy's hosted service.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
