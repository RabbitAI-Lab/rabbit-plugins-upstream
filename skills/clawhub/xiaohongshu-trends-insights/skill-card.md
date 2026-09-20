## Description:

Helps agents collect structured public Xiaohongshu note, comment, creator-post, and interaction data for trend insight, content planning, competitor monitoring, and marketing research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content operators, brand researchers, creators, and marketing analysts use this skill to query public Xiaohongshu content by keyword, note link, or creator profile and feed structured results into topic research, trend tracking, KOL screening, and comment analysis workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Complete Xiaohongshu API results may be saved automatically to a shared temporary log location, exposing sensitive market research on shared machines.

Mitigation: Run only on trusted machines, protect or clear local logs after use, and avoid confidential targets unless local retention is acceptable.

Risk: Search keywords and Xiaohongshu links are sent to guaikei.com through authenticated API requests.

Mitigation: Use an approved API token, avoid submitting confidential targets, and confirm that this data flow is acceptable for the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/xiaohongshu-trends-insights)
- [Server-resolved GitHub import](https://github.com/why20261/xiaohongshu-trends-insights)
- [Homepage from ClawHub metadata](https://github.com/um-why/xiaohongshu-openclaw-skill)
- [GuaiKei API token provider](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Troubleshooting reference](references/troubleshooting.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Node.js shell commands; command results are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN. Commands may save complete API results to local temporary logs.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact declares 1.1.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
