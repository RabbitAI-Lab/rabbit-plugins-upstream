## Description:

Searches Pixabay Music for royalty-free background tracks and returns track links and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents use this skill to find background music by short English style keywords and review matching track links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to the dLazy hosted API.

Mitigation: Use only when sending search terms to api.dlazy.com is acceptable.

Risk: The broader CLI can upload local media and save downloaded assets to disk.

Mitigation: Avoid local file paths unless uploads are intended, and review download destinations before using --save.

Risk: The CLI stores an API key for authenticated requests.

Mitigation: Protect the stored key and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with track links and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on short English search terms; an API key is required.]

## Skill Version(s):

1.3.29 (source: ClawHub release; bundled skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
