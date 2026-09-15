## Description:

Generate realistic digital human broadcast videos from portrait images and audio/text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to call the dLazy CLI for generating digital human broadcast videos from a portrait image plus audio or text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a pinned third-party npm package and hosted dLazy API service.

Mitigation: Install only after reviewing the linked CLI source or npm package; prefer npx or another ephemeral invocation pattern when long-term global installation is unnecessary.

Risk: Prompts, selected media files, and the dLazy API key are sent to or used with external dLazy endpoints.

Mitigation: Use only data appropriate for the dLazy service, store credentials through the documented CLI mechanisms, and rotate the API key if exposure is suspected.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return generated asset URLs, async task identifiers, or saved local files when requested.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
