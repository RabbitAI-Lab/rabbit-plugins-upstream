## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition. Suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate commercial-grade Seedream 5.0 Pro images from text prompts and optional reference images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images are sent to dLazy's hosted service for generation.

Mitigation: Avoid using sensitive prompts or files unless their disclosure to the third-party service is acceptable.

Risk: The skill requires a dLazy API key and may store it in the local CLI configuration.

Mitigation: Use the documented authentication flow, protect the local configuration file, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Global installation persists a third-party CLI on the system.

Mitigation: Prefer the documented npx invocation for non-global use when a persistent CLI install is unnecessary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to invoke dLazy CLI commands that return hosted image-generation results, including image URLs or asynchronous task identifiers.]

## Skill Version(s):

1.2.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
