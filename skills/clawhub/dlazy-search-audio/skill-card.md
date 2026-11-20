## Description:

Audio search tool: searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can search for royalty-free background music with a few short English style keywords, then review track URLs and metadata to choose audio for their project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised Pixabay Music search behavior was not demonstrated, and the scanner noted a mismatch with the reported CLI authentication behavior.

Mitigation: Before relying on search results, verify that the pinned CLI version performs the documented search and returns the expected track URLs.

Risk: The referenced CLI package and several local references were not inspected, so the available security evidence is incomplete.

Mitigation: Review the pinned CLI package and referenced materials before installing or relying on the integration.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI source link declared in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [JSON, Audio track URLs, Track metadata]

**Output Format:** [JSON search results containing track URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are links and metadata; downloading a track is an optional separate action.]

## Skill Version(s):

1.3.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
