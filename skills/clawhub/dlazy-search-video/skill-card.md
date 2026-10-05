## Description:

Searches for stock video footage by keyword and returns video URLs and metadata through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find stock video footage and inspect matching video URLs and metadata for their projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider and data-flow descriptions are inconsistent; searches and parameters are shared with dLazy, not only Pixabay.

Mitigation: Review the dLazy service boundary before installing and avoid sending sensitive queries or parameters.

Risk: The CLI may upload supplied local media paths and uses a dLazy API key.

Mitigation: Provide local paths only when intended, keep the API key private, and rotate or revoke it if exposed.

Risk: A global CLI installation persists locally, and --save writes downloaded assets to disk.

Mitigation: Use the pinned npx invocation for a smaller local footprint and approve explicit --save destinations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON search results containing video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID instead of search results.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
