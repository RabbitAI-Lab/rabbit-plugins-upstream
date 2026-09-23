## Description:

Audio generation skill that selects an appropriate dLazy CLI audio or text-to-speech model from the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate speech, music, dialogue, and sound effects through the dLazy CLI. The skill guides the agent to choose a suitable audio model, inspect its parameters, and run the matching command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected media may be uploaded to dLazy hosted services for generation.

Mitigation: Use only content approved for external processing and review dLazy terms and organizational data-handling requirements before use.

Risk: Authentication through the CLI can save a dLazy API key in the local user config.

Mitigation: Use the DLAZY_API_KEY environment variable per invocation when a persistent local key is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a pinned third-party npm CLI package.

Mitigation: Review the pinned @dlazy/cli package and source before installation when supply-chain assurance is required.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration, JSON]

**Output Format:** [Markdown guidance with inline bash commands and CLI JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated audio or media URLs hosted by dLazy; requires npm or npx and a dLazy API key.]

## Skill Version(s):

1.3.20 (source: server release evidence; artifact frontmatter lists 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
