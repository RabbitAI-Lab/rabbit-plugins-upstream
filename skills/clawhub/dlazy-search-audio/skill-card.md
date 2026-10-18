## Description:

Searches Pixabay Music for royalty-free background tracks and returns track links and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find background music by short style keywords and review track links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and parameters are sent to the dLazy service.

Mitigation: Review requests before submission and avoid including sensitive information.

Risk: Using the CLI requires installing a package and storing a dLazy API key locally.

Mitigation: Review the pinned CLI before installation and protect or revoke the key when appropriate.

Risk: Local file paths or save/upload options can cause files or outputs to be handled by the dLazy service.

Mitigation: Do not use file paths or save/upload options unless that handling is intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata link)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Track links and metadata; asynchronous requests can return a task ID instead.]

## Skill Version(s):

1.3.31 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
