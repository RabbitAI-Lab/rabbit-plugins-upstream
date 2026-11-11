## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and developers can search for stock video footage by keyword and narrow results by video type, category, or duration. The skill returns video URLs and related metadata through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the stated Pixabay video-search purpose and the documented commands, and the external CLI's role is unclear.

Mitigation: Review the pinned @dlazy/cli release and confirm what `dlazy search_video` sends and returns before authenticating.

Risk: The skill requires a dLazy API key and documents sending search parameters to dLazy's hosted API.

Mitigation: Use credentials only with an account you trust, and avoid including sensitive information in search queries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Video URLs, Video metadata]

**Output Format:** [JSON response containing search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be filtered by video type, category, duration, and pagination.]

## Skill Version(s):

1.3.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
