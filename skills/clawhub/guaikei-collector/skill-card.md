## Description:

guaikei-collector helps agents retrieve public Xiaohongshu notes, note details, comments, and creator posts through Guaikei for content research, competitive monitoring, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, analysts, and content creators use this skill to collect public Xiaohongshu data by keyword, note URL, or profile URL. Agents can then summarize, compare, or report on the structured results for content planning, KOL screening, trend analysis, and competitive monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords and URLs are sent to the Guaikei API service.

Mitigation: Use only public, non-sensitive Xiaohongshu queries and links, and confirm that the data-sharing posture is acceptable before running commands.

Risk: Returned results are saved in local JSON log files.

Mitigation: Store logs according to team retention rules and delete them when the collected data is no longer needed.

Risk: The collected public data could be redistributed or used outside the allowed analysis context.

Mitigation: Limit use to public Xiaohongshu data, avoid private or login-only content, and review outputs before sharing or republishing.

## Reference(s):

- [Guaikei website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [README](readme.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON from Node.js CLI commands, including status, request metadata, and returned Xiaohongshu results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes JSON result logs locally.]

## Skill Version(s):

1.0.0 (source: server release evidence, SKILL.md metadata, package.json, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
