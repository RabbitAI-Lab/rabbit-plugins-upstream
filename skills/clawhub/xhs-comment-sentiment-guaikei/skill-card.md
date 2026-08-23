## Description:

This command skill retrieves public Xiaohongshu keyword results, note details, comments, and creator posts through guaikei.com for trend monitoring and comment sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand marketers, market researchers, and analysts use this skill to fetch public Xiaohongshu search results, note details, comments, and creator-post listings for content planning, competitor monitoring, KOL screening, trend tracking, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or URLs to guaikei.com.

Mitigation: Use it only for user-directed public-data analysis and confirm that sending those inputs to the third-party service is approved.

Risk: Returned public data, including comments or business research results, may be retained locally in generated logs.

Mitigation: Periodically delete generated logs and avoid retaining sensitive research outputs longer than needed.

Risk: The top-level description may understate broader comment and profile collection behavior.

Mitigation: Review the full capability scope before enabling the skill and keep usage limited to public Xiaohongshu data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-comment-sentiment-guaikei)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
