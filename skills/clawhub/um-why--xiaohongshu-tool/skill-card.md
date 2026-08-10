## Description:

小红书数据洞察与竞品分析助手 helps agents search public Xiaohongshu notes, retrieve note details and comments, and collect public creator post lists for content research, competitive analysis, KOL screening, and trend insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

Content creators, brand marketers, and market analysts use this skill to gather structured public Xiaohongshu data for topic research, competitor monitoring, comment analysis, creator evaluation, and follow-on reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and Xiaohongshu links are sent to the disclosed third-party Guaikei API together with the configured API token.

Mitigation: Use the skill only when that data sharing is acceptable, keep GUAIKEI_API_TOKEN restricted to trusted environments, and avoid submitting sensitive or unnecessary inputs.

Risk: Returned public posts and comments can be saved under the package logs directory.

Mitigation: Limit collection to the task need, restrict access to generated logs, and delete logs when they are no longer needed.

Risk: The skill is intended for public Xiaohongshu data and may fail or return no usable result for private, deleted, unavailable, or unsupported links.

Mitigation: Confirm that inputs are public Xiaohongshu note or creator profile links, check status and error_code before analysis, and do not fabricate results for empty or error responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/um-why/skills/xiaohongshu-tool)
- [Guaikei API token service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Structured JSON results with concise Markdown or text summaries and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supported commands return status, error_code, request metadata, runtime metadata, and results when available.]

## Skill Version(s):

1.1.1 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
