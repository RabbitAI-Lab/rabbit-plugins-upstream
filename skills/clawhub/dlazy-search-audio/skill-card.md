## Description:

Searches Pixabay Music and returns royalty-free music track URLs and metadata for choosing background music.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can search Pixabay Music for suitable background tracks using short English style keywords, then review track links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests use dLazy rather than connecting directly to Pixabay and may consume account credits.

Mitigation: Review the query and any applicable credit cost before running the search.

Risk: Authentication stores an organization API key in local CLI configuration, or accepts it through DLAZY_API_KEY.

Mitigation: Use a protected user account, avoid exposing the key, and rotate or revoke it if necessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Audio files]

**Output Format:** [Structured search results containing music track URLs and metadata; optionally a downloaded audio file when a save path is provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches work best with 2–3 short English style keywords; results may also be saved locally.]

## Skill Version(s):

1.3.34 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
