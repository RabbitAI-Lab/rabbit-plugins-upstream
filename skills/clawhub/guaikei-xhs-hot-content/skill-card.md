## Description:

This command skill retrieves public Xiaohongshu search, note, comment, and creator-post data through the Guaikei API for trend monitoring, content research, competitor analysis, and downstream reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, and analysts use this skill to collect public Xiaohongshu keyword results, note details, comments, and creator posts for content planning, trend monitoring, competitive research, and report generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note URLs, profile URLs, and GUAIKEI_API_TOKEN to a third-party API service.

Mitigation: Use it only when that data egress is acceptable, avoid sensitive research terms where possible, and keep the API token scoped and rotated according to local policy.

Risk: Returned public content and comments are saved under the local logs directory.

Mitigation: Review log contents before sharing, store them according to the user's data handling requirements, and delete logs that are no longer needed.

Risk: The skill is intended for public Xiaohongshu data and may be misused for private, restricted, or noncompliant collection.

Mitigation: Use only public data, do not attempt to access private or login-required content, and respect Xiaohongshu rules and applicable law.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-hot-content)
- [Guaikei API site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON on stdout with local JSON log files; guidance is Markdown-style prose with command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; sends Xiaohongshu keywords, note/profile URLs, and the API token to guaikei.com; saves returned public content and comments under the skill's local logs directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
