## Description:

Searches public Xiaohongshu posts by keyword or URL, retrieves note details, comments, and blogger posts, and returns structured interaction data for trend, content, competitor, and KOL research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content teams, marketers, and analysts use this skill to collect public Xiaohongshu search results, note details, comments, and blogger post lists for content research, trend monitoring, competitor analysis, and KOL screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords, Xiaohongshu URLs, request limits, and the GUAIKEI API token are sent to guaikei.com over HTTPS.

Mitigation: Use the skill only when that data sharing is approved, keep the API token in environment configuration, and avoid placing secrets in prompts or shared outputs.

Risk: Large public-data pulls can collect up to 10000 notes, comments, or posts and successful results may be retained in local logs.

Mitigation: Limit collection to the needed scope, follow applicable platform and organizational rules, and delete retained logs when they are no longer needed.

Risk: The skill depends on a third-party API and can return empty or error statuses when authentication, platform data, or service availability fails.

Mitigation: Treat empty and error statuses as failures to resolve rather than evidence, and retry or adjust inputs according to the documented error guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-check-blogger)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON from Node.js CLI commands, with status fields and local log files for successful results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and public Xiaohongshu keyword or URL inputs; successful results may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
