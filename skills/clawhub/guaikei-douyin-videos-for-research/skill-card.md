## Description:

This skill lets an agent run Node.js commands to search Douyin content, fetch public creator posts and video comments, and retrieve real-time trending topics for short-video research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and research teams use this skill to collect public Douyin search results, creator posts, comments, and trending topics for content research, competitor analysis, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger rules may route vague requests into Douyin public-data research through a third-party API.

Mitigation: Use the skill only after confirming the user intends GUAIKEI-backed Douyin research and has supplied an appropriate public keyword, account, video, or trending-topic request.

Risk: Fetched comments, account URLs, or search topics can be retained in the generated logs directory.

Mitigation: Delete logs periodically and avoid submitting confidential research targets or sensitive monitoring subjects.

Risk: Collected platform data may be subject to Douyin terms, privacy expectations, and local law.

Mitigation: Limit use to compliant public-data research and avoid redistribution or uses beyond the user's authorized internal analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-videos-for-research)
- [Usage documentation](readme.md)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [GUAIKEI service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON on stdout with status and logs on stderr; fetched results may also be written to local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN. The skill can save fetched public-data results under logs/ by default.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
