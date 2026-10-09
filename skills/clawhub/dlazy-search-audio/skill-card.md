## Description:

Searches Pixabay Music for royalty-free background tracks and returns track URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents help users find royalty-free background music by searching for short style keywords and returning track links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reviewed release is flagged as suspicious: its audio-search description also discusses cloud uploads, downloads, and generation features.

Mitigation: Review the pinned dLazy CLI package and confirm the command's behavior before using it.

Risk: Search inputs and any supplied local media may be sent to dLazy services, and the CLI needs an API key.

Mitigation: Provide only intended inputs, avoid local media paths unless cloud processing is wanted, and use a revocable API key.

Risk: Save and asynchronous options can download files or start tasks beyond a simple immediate search.

Mitigation: Avoid save and async options unless explicitly needed; check the request with dry-run first.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (declared in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON search results with track URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of immediate results.]

## Skill Version(s):

1.3.27 (source: ClawHub release; bundled frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
