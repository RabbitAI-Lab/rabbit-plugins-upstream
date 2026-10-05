## Description:

Searches Pixabay Music for background tracks and returns audio links and track metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find background music by style, duration, and result count.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the hosted CLI requires a dLazy API key and sends search parameters to dLazy.

Mitigation: Use only if comfortable with the hosted service and protect the API key.

Risk: The instructions also describe uploading local media paths, beyond audio search.

Mitigation: Do not provide local file paths unless an upload is intentional.

Risk: The optional --save flag writes a downloaded asset locally.

Mitigation: Use --save only with an explicit destination path you trust.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [Skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include track URLs and metadata; optional --save downloads to a local path.]

## Skill Version(s):

1.3.26 (source: server release metadata; embedded frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
