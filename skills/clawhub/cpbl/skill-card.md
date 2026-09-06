## Description:

Query CPBL scores, schedules, live games, standings, player statistics, advanced Statcast-style data, news, and Taiwan baseball history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ichendong](https://clawhub.ai/user/ichendong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer Chinese Professional Baseball League questions and run bundled scripts for scores, schedules, standings, statistics, advanced metrics, news, and historical facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports browser automation to access an anti-bot protected Taiwan baseball wiki.

Mitigation: Review source terms before use, prefer official or permitted data sources, and reserve this path for historical questions that official sources cannot answer.

Risk: The skill makes direct CPBL AJAX requests with CSRF tokens and may write a temporary token cache in shared temporary storage.

Mitigation: Run it in an isolated agent environment, avoid storing unrelated secrets in shared temporary paths, and clear temporary state after use when appropriate.

Risk: Sports data can be delayed, partial, or affected by brittle upstream endpoint behavior.

Mitigation: State freshness limits in user-facing answers and verify important results against official CPBL pages or announcements.

## Reference(s):

- [ClawHub CPBL skill page](https://clawhub.ai/ichendong/cpbl)
- [CPBL API endpoint notes](references/api-endpoints.md)
- [CPBL skill summary](references/summary.md)
- [CPBL test report](references/test-report.md)
- [CPBL official news](https://cpbl.com.tw/news)
- [CPBL official standings](https://www.cpbl.com.tw/standings/season)
- [Taiwan Baseball Wiki](https://twbsball.dils.tku.edu.tw/wiki/index.php)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or plain text responses with optional JSON script output and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and uv; some historical-data flows may use browser automation, and some CPBL AJAX flows use a temporary CSRF token cache.]

## Skill Version(s):

2.0.0 (source: server release metadata and skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
