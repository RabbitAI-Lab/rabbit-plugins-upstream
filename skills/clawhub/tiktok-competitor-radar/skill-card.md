## Description:

Retrieves public TikTok posts and comments by keyword, creator, or video to support competitor and brand analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Brand, marketing, and research teams use public TikTok post and comment data to compare competitors, identify creators, and track content trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API tokens and TikTok query details are sent to guaikei.com.

Mitigation: Use only with an approved token and avoid submitting sensitive search terms or identifiers.

Risk: Saved results can include public comments and user identifiers.

Mitigation: Restrict access to local result logs and delete them when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/tiktok-competitor-radar)
- [Usage and options](references/options.md)
- [Guaikei data service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON data, Analysis guidance]

**Output Format:** [Structured JSON for posts and comments; optional narrative comparisons by the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public TikTok data; command results may also be saved as local JSON logs.]

## Skill Version(s):

1.0.0 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
