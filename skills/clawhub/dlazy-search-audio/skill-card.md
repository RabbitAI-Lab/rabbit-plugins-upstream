## Description:

Audio search tool: searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and their agents use this skill to search Pixabay Music for background tracks with short English style keywords and receive track URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search inputs are sent to dLazy, and local media passed through the CLI may be uploaded to its storage.

Mitigation: Avoid sensitive search terms and provide only files intended for upload.

Risk: The external CLI and hosted service were not audited; use may consume organization credits, and the documented example conflicts with the listed options.

Mitigation: Review the CLI before installation, protect and rotate the organization API key as needed, monitor credit use, and check command help before use.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)

## Skill Output:

**Output Type(s):** [JSON, Audio track URLs, Track metadata]

**Output Format:** [JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return multiple tracks; asynchronous mode can return a task identifier and status.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
