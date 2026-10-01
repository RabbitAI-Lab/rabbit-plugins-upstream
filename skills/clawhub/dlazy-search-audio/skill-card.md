## Description:

Searches Pixabay Music for royalty-free tracks and returns links and metadata to help select background music.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers search for background music using short English style keywords and optional duration filters, then review track links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to dLazy, and broader CLI options may upload local files.

Mitigation: Use only queries suitable for sharing with dLazy and avoid local file paths unless an upload is intended.

Risk: The CLI can save an API key locally or download results to a chosen path.

Mitigation: Use a per-invocation API key when local storage is unwanted, and review any download path before using --save.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with track URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search responses include track links and metadata; asynchronous requests may require a separate status check.]

## Skill Version(s):

1.3.24 (source: ClawHub release evidence; source skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
