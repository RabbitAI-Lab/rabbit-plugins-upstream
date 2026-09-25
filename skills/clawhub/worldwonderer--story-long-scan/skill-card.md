## Description:

Analyzes Chinese web-novel rankings to identify genre trends and practical long-form story ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and publishing teams use this skill to examine rankings on Chinese web-novel platforms, identify recurring reader interests, and choose feasible long-form fiction topics. It can collect public ranking pages or analyze user-provided data, then prepare reports and topic recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collecting ranking pages may conflict with a site's terms or collect more data than needed.

Mitigation: Confirm the target platform and review site terms before collection; limit collection to necessary public ranking data.

Risk: Browser-based collection may use an existing browser session.

Mitigation: Confirm whether to connect to an existing browser session before running browser-based collection.

Risk: Sparse or incomplete rankings can lead to misleading trend recommendations.

Mitigation: Review data-quality labels and validate trends against multiple recent samples before relying on recommendations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/story-long-scan)
- [Project link listed in skill metadata (unverified provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Ranking data and report format](references/scan-output-format.md)
- [Topic selection guidance](references/topic-decision.md)
- [Genre trend guidance](references/genre-trends.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown ranking summaries, trend reports, and topic recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write dated ranking reports and a topic-decision file to the selected local output directory; reports should identify sparse or incomplete data.]

## Skill Version(s):

1.1.14 (source: ClawHub release evidence; bundled skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
