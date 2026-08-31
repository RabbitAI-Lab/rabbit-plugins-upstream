## Description:

This skill helps an agent collect public Douyin data for keyword search, creator posts, video comments, and real-time trending topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Douyin content, compare creator activity, analyze video comments, and track trending topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad natural-language triggers can start collection for requests that only loosely resemble Douyin research.

Mitigation: Confirm that the user intends a Douyin public-data task before running a CLI command.

Risk: Token-backed requests send search terms, creator URLs, or video URLs to guaikei.com.

Mitigation: Keep GUAIKEI_API_TOKEN private and avoid using sensitive research terms or URLs unless that disclosure is acceptable.

Risk: Scraped results are saved locally by default and may contain research targets or comments.

Mitigation: Review and delete generated logs when they are no longer needed, especially on shared machines.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-info-scraper)
- [README](readme.md)
- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [Structured JSON on stdout and timestamped JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and supports search, creator-post, comment, and hot-list modes.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
