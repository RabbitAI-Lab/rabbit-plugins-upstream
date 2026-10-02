## Description:

Analyzes rankings across Chinese web-fiction platforms to identify long-form genre trends and promising story concepts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Web-fiction writers and editors use this skill to compare platform rankings, assess genre demand, and choose feasible long-form story topics backed by available samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ranking collection may conflict with a platform's scraping terms.

Mitigation: Check the target site's terms before collecting rankings.

Risk: Browser-based collection may use an existing site session.

Mitigation: Use a separate browser profile when existing sessions should remain isolated.

Risk: Scan results write local reports and may reflect incomplete or stale rankings.

Mitigation: Run in a workspace where scan-output files are acceptable, and verify sparse or outdated samples before making decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/story-long-scan)
- [Project link listed in skill metadata (provenance unverified)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Topic decision guide](artifact/references/topic-decision.md)
- [Genre trends reference](artifact/references/genre-trends.md)
- [Reader profiling reference](artifact/references/reader-profiling.md)
- [Platform and publishing guide](artifact/references/publishing-guide.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown ranking summaries, trend reports, and story-topic recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports and topic decisions may be saved as local Markdown files.]

## Skill Version(s):

1.1.16 (source: ClawHub release metadata; bundled frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
