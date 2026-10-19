## Description:

Searches Pixabay Music for royalty-free background music and returns track links and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find background music by short English style keywords and review track links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised music search uses a broader hosted CLI that can send prompts and supplied media to dLazy.

Mitigation: Review the CLI before installation; use the documented query-only search flow and avoid supplying private prompts or media.

Risk: The CLI can store a dLazy API key locally and download assets to a chosen path.

Mitigation: Protect or rotate the key and confirm any download path before saving files.

Risk: Async generation and file-upload options exceed the needs of a simple music search.

Mitigation: Prefer a search-only implementation if broader hosted API features are not needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text summarizing JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Track URLs and metadata; asynchronous requests may return a task ID instead of results.]

## Skill Version(s):

1.3.32 (source: server release metadata; bundled skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
