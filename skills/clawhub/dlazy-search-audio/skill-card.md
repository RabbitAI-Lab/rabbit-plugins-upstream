## Description:

Audio search tool: searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can find background music by searching Pixabay Music with a few short English style keywords, then review track URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a dLazy API key, and the skill sends search requests to dLazy-hosted services.

Mitigation: Use an account-scoped key, review dLazy's service terms, and rotate or revoke the key if it is exposed.

Risk: The security scan was partial because several local references could not be resolved.

Mitigation: Review the CLI and its dependencies before installation or use.

## Reference(s):

- [CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Audio URLs, Track metadata]

**Output Format:** [JSON search results containing track URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search with 2–3 short English style keywords; long phrases may return no results.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
