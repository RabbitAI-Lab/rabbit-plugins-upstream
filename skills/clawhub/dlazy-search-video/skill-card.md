## Description:

Searches for stock video footage by keyword and returns video URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents use this skill to find stock video footage by keyword and review video links and metadata for sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search inputs are sent to dLazy, and use requires a locally stored dLazy API key.

Mitigation: Avoid sensitive search inputs, protect the API key, and rotate or revoke it if exposed.

Risk: The documentation also describes local media uploads, although their relevance to video search is unclear.

Mitigation: Do not pass local media paths until the publisher clarifies when files are uploaded and why.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Video search results with URLs and metadata in JSON or summarized text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; searches may return an asynchronous task identifier.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
