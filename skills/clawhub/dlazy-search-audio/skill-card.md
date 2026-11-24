## Description:

Audio search tool: searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and other users can search for background music by short English style keywords and review track links and metadata returned to the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The music-search description and the dLazy login or authentication steps and external CLI may not match a user's expectations; some referenced package details were unavailable to the scanner.

Mitigation: Before installing or authenticating, review the pinned dLazy CLI package and confirm that its login flow and service match the intended Pixabay music search use.

## Reference(s):

- [dLazy CLI project homepage (metadata.clawdis)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm (metadata.clawdis)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON result envelope with track URLs and metadata, plus concise search guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Use 2–3 short English style keywords; each track URL is in the url field.]

## Skill Version(s):

1.3.44 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
