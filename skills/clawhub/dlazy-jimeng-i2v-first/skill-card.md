## Description:

Generate dynamic videos from a single first-frame image and prompt using the Jimeng image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and agents use this skill to invoke the dLazy CLI for Jimeng first-frame image-to-video generation from a prompt and an input image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local first-frame image inputs are sent to dLazy's hosted service for generation.

Mitigation: Avoid submitting sensitive content unless the user has approved the service use and data handling.

Risk: A global npm install persists a third-party CLI binary on the user's system.

Mitigation: Prefer the pinned npx invocation for temporary use, or review the linked dLazy CLI source and package before global installation.

Risk: The CLI can save the dLazy API key in a local configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI Repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Invokes a pinned dLazy CLI that can return hosted generated-video URLs or asynchronous task identifiers.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
