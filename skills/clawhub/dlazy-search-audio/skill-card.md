## Description:

Audio search tool that searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find royalty-free background music by short English style keywords and return track URLs with metadata for selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a hosted dLazy service and npm CLI, so prompts, parameters, and intended media inputs may leave the local environment.

Mitigation: Use it only when cloud processing is acceptable, and avoid passing sensitive local file paths unless upload is intended.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-run `DLAZY_API_KEY` or `npx @dlazy/cli@1.2.3` when persistent global install or saved credentials are not desired.

Risk: The artifact documentation is inconsistent about whether the audio search command expects `--query` or `--prompt`.

Mitigation: Check `dlazy search_audio -h` before invocation and prefer the command help over examples if they conflict.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON result wrapped by CLI output, with track URLs and metadata in the result payload]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports duration and result-count filters; asynchronous invocation may return a task identifier for polling.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
