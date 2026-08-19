## Description:

Searches Pixabay Music for royalty-free audio tracks and returns track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-producing agents use this skill to search for royalty-free background music by short English style keywords and retrieve usable track metadata and URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy account/API key and sends search parameters to dLazy.

Mitigation: Use non-sensitive search terms and configure credentials only through the documented dLazy CLI flow or per-invocation environment variable.

Risk: The optional --save behavior can create or overwrite files at a user-selected destination.

Mitigation: Use --save only with destination paths that are intended for downloaded results and safe to create or overwrite.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON responses with royalty-free audio track URLs and metadata, plus concise command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches use short English style keywords; optional duration and page-size parameters can refine results.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
