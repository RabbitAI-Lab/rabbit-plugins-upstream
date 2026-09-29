## Description:

Searches Pixabay Music for royalty-free background tracks and returns track URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find background music by searching Pixabay Music with short English style keywords and reviewing track links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search inputs are sent to dLazy servers.

Mitigation: Avoid submitting confidential queries or private local files unless sharing them with the service is intended.

Risk: The external CLI may store a dLazy API key in local configuration.

Mitigation: Protect the local configuration and review the pinned CLI package before installation; use the on-demand npx option to avoid a persistent global install.

## Reference(s):

- [dLazy CLI source (artifact metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON search results containing audio track URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Track links appear in each hit's url field; a dLazy API key is required.]

## Skill Version(s):

1.3.23 (source: server-resolved release; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
