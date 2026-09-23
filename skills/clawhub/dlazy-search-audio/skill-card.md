## Description:

Audio search tool that searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to find royalty-free background music by short English style keywords and retrieve track URLs plus metadata for downstream media workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy CLI and API key, so search text and explicitly supplied files may be sent to dLazy services.

Mitigation: Avoid sensitive prompts or files unless you intend to send them to dLazy, and rotate or revoke the API key from the dLazy dashboard when access should change.

Risk: A global CLI install persists a third-party executable on the user's system.

Mitigation: Use the pinned npx invocation for one-off runs when a persistent global install is not needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [json, shell commands, guidance]

**Output Format:** [JSON result objects with track URLs and metadata, plus shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries should use 2-3 short English style keywords; long phrases may return zero results.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
