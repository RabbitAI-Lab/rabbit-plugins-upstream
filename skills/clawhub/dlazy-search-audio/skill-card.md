## Description:

Searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can search for background music by entering short English style keywords, then use the returned track URLs and metadata to choose a track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was benign at medium confidence, with partial coverage and a reported mismatch between authentication/login commands and the described music search.

Mitigation: Review the CLI behavior and confirm its login and authentication steps before installation; use a scoped API key and revoke it if needed.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)

## Skill Output:

**Output Type(s):** [JSON, API results]

**Output Format:** [JSON containing track URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Use 2–3 short English style keywords; long phrases may return no results. Each track URL is in the url field.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
