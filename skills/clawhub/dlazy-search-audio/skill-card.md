## Description:

Searches Pixabay Music for royalty-free audio tracks and returns track links and metadata for background music selection.

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

Risk: Authentication requires a dLazy API key that the CLI may store locally.

Mitigation: Protect the local CLI configuration and rotate or revoke the key if exposed.

Risk: Queries and parameters are sent to dLazy, and local media paths passed to the CLI may cause file uploads.

Mitigation: Review inputs before running the command; avoid private file paths unless an upload is intended.

Risk: The CLI can save downloaded results to a local path.

Mitigation: Choose a specific, trusted save location before downloading.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON audio-search results or a natural-language summary of track links and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of immediate results.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
