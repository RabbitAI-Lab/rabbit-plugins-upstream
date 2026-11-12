## Description:

Analyzes short-fiction samples from Chinese writing platforms to identify emerging themes and suggest ways to validate story ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External writers use this skill to review short-fiction market samples, compare platform patterns, and develop topic ideas that fit their materials and submission requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks this release suspicious, reporting behavior that may not match its stated popularity-analysis purpose and noting that parts of the scripts were only partially inspected.

Mitigation: Follow the scan guidance and defer installation until the publisher explains the authenticated catalog access and aligns the description with the behavior.

Risk: Heiyan collection requires a logged-in admin session; the script reads its Admin-Token cookie and uses it to request catalog data.

Mitigation: Use only an authorized account in a browser session you control, and review the collection scripts before running them.

## Reference(s):

- [Manual Rank Input](references/manual-rank-input.md)
- [Dianzhong Platform Guide](references/platform-dianzhong.md)
- [Heiyan Platform Guide](references/platform-heiyan.md)
- [Historical Market Notes](references/real-market-data.md)
- [Topic Matching Guide](references/topic-match.md)
- [Project link from skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-short-scan)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Files]

**Output Format:** [Markdown report with ranking tables, market observations, and topic recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports identify sample dates, coverage, confidence, and a suggested rescan date; historical patterns are labeled as unverified candidates.]

## Skill Version(s):

1.1.22 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
