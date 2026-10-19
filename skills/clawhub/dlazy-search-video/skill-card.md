## Description:

Searches for stock video footage by keyword and returns video URLs and metadata through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find stock video footage for media projects by keyword, category, and duration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes Pixabay search but routes requests through a broader dLazy cloud service.

Mitigation: Confirm the service and actual search_video help output before relying on the examples or sending queries.

Risk: Using the skill requires a dLazy API key and sends search inputs or referenced media to dLazy.

Mitigation: Treat dLazy as a trusted service only after review; protect the key and avoid submitting private local files.

Risk: A global CLI installation persists on the local system.

Mitigation: Prefer the version-pinned npx invocation when a persistent installation is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON search results containing video URLs and metadata, suitable for a text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task identifier instead of results.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; supplied skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
