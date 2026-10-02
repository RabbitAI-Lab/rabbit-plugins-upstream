## Description:

Searches stock videos by keyword through the dLazy CLI and returns video URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to find stock video footage by keyword and review result URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search prompts and parameters are sent to dLazy services rather than directly to Pixabay.

Mitigation: Use only if sharing the search inputs with dLazy is acceptable; avoid sensitive prompts.

Risk: Using the third-party CLI requires an API key and may transmit local files or sensitive save paths.

Mitigation: Prefer the pinned on-demand CLI, use a scoped and revocable API key, and avoid passing sensitive files or save paths.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Video URLs and metadata]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous searches may return a task ID instead of immediate results.]

## Skill Version(s):

1.3.25 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
