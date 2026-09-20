## Description:

Text-to-image generation with Jimeng that converts prompts into generated image outputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent generate Jimeng text-to-image assets from prompts, optionally with reference images and local save paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media paths may be sent to dLazy's hosted API and media storage.

Mitigation: Avoid submitting private prompts or files unless intended, and review the service terms before using the hosted generation workflow.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Use trusted machines for saved credentials, use DLAZY_API_KEY for one-off invocations when appropriate, and rotate or revoke keys from the dLazy dashboard if needed.

Risk: A global install persists the dLazy CLI on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution if a persistent global CLI install is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown instructions with bash commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs and can be saved to a local path with --save.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
