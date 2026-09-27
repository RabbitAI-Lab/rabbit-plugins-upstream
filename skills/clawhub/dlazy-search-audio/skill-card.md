## Description:

Audio search tool that searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content creators use this skill to find royalty-free background music by issuing short English style-keyword searches through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy CLI and hosted API, so search prompts and explicitly supplied media paths may be sent to dLazy-hosted services.

Mitigation: Use the skill only for data appropriate for dLazy-hosted processing, and review the dLazy service terms before operational use.

Risk: Authentication can persist an API key in the local dLazy configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run authentication when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: The artifact contains inconsistent option examples for the search query flag.

Mitigation: Run dlazy search_audio -h and confirm whether the installed CLI expects --query or --prompt before relying on examples.

Risk: Global installation creates a persistent third-party CLI binary on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution when a persistent global install is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI source link from skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are returned by the dLazy CLI as JSON containing output objects, track metadata, and URLs; asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.21 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
