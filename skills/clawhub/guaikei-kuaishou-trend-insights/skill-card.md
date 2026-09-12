## Description:

Retrieves public Kuaishou video search results, creator posts, and video comments through Guaikei's API so agents can return structured data for trend research, competitor monitoring, KOL screening, comment analysis, and content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content teams, marketers, data analysts, and agents use this skill to collect public Kuaishou data for keyword trend research, creator monitoring, video comment review, and downstream reporting. The skill requires a GUAIKEI_API_TOKEN and sends query inputs to guaikei.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile URLs, video URLs, query parameters, and the API token are sent to the third-party Guaikei service.

Mitigation: Use the skill only with data you are authorized to submit to guaikei.com, and provide a scoped GUAIKEI_API_TOKEN through the environment rather than embedding it in prompts or files.

Risk: Command results are saved locally under logs/ and may reveal research targets, competitor monitoring activity, or collected comment datasets.

Mitigation: Treat generated logs as sensitive work history, restrict access to the workspace, and delete logs when they are no longer needed.

Risk: The skill is limited to public Kuaishou data and may return empty results or service errors for unavailable, deleted, private, or rate-limited targets.

Mitigation: Check the returned status and error_code before using results in reports, and avoid fabricating conclusions when results are empty or errors occur.

## Reference(s):

- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei API Service](https://www.guaikei.com)
- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-trend-insights)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and structured JSON command results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful commands return status, error_code, message, timestamp, request, skill_metadata, and results; command outputs may also be saved under logs/.]

## Skill Version(s):

1.0.0 (source: SKILL.md metadata, package.json, changelog, and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
