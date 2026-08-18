## Description:

Searches Xiaohongshu public notes, note details, comments, and creator posts through Guaikei's API and returns structured data for trend, competitor, KOL, and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Content, marketing, and research teams use this skill to collect public Xiaohongshu notes, comments, interaction metrics, and creator posts for topic discovery, competitor monitoring, KOL screening, and follow-on reporting. It requires a GUAIKEI_API_TOKEN and does not support private, hidden, login-only, publishing, or interaction workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note or profile URLs, requested limits, and the GUAIKEI_API_TOKEN to the guaikei.com service.

Mitigation: Use it only when that third-party data sharing is acceptable, scope tokens appropriately, and avoid submitting private, confidential, or login-only data.

Risk: The skill writes retrieved results to local JSON logs that may contain sensitive business research.

Mitigation: Store logs in an approved location, restrict access, and delete or archive them according to the user's data retention policy.

Risk: The skill is limited to public Xiaohongshu lookup workflows and can fail on missing tokens, invalid links, empty results, rate limits, or upstream service errors.

Mitigation: Validate required inputs before execution, inspect status and error_code fields before using results, and do not treat failed or empty responses as factual analysis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-trending-finder)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI executions return structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include public Xiaohongshu content, comments, author metadata, interaction metrics, request metadata, and locally written JSON logs.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact metadata lists 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
