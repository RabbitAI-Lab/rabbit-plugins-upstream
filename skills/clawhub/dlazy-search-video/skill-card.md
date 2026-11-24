## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and agents can search for stock footage by keyword, filter by video type, category, or duration, and use returned video URLs and metadata to source clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan noted a mismatch between the stated Pixabay video-search purpose and the dLazy CLI setup and invocation; the CLI's internal behavior was not reviewed.

Mitigation: Before installing, review the dLazy CLI and decide whether its setup and use are acceptable; a benign scan rating does not guarantee safety.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI source link listed in skill metadata (not server-verified provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [JSON, text, guidance]

**Output Format:** [JSON search results with stock video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be filtered by video type, category, duration, page, and page size.]

## Skill Version(s):

1.3.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
