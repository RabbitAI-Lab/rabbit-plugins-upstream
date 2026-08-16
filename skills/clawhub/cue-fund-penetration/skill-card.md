## Description:

Uses Cue to analyze public A-share fund portfolios by looking through disclosed holdings, identifying overlapping positions, industry concentration, style exposure, and concentration risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External fund investors, investment advisors, and portfolio researchers use this skill to diagnose whether a group of public A-share funds is genuinely diversified or concentrated in the same stocks, industries, styles, or managers. It supports portfolio health checks, fund selection de-duplication, recurring investment reviews, and client-facing diagnostic reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fund lists, portfolio composition, and client-related details are sent to Cue's external service.

Mitigation: Use sanitized inputs where possible, avoid personal identifiers or confidential client data unless authorized, and protect the Cue API key.

Risk: Generated allocation suggestions may be mistaken for automatic investment instructions.

Mitigation: Treat outputs as research support and have a qualified human review any proposed portfolio changes before acting.

Risk: Holdings analysis can be stale because public fund disclosures are periodic rather than real time.

Mitigation: Label reports with the disclosure or data cutoff date and avoid using the results for short-term trading decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fund-penetration)
- [Cue skills runner source](https://github.com/sensedeal/cue-skills)
- [Cue skills runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key portal](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown diagnostic report with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may take 2-15 minutes depending on portfolio size and Cue service load; analysis relies on public quarterly or annual fund holdings disclosures and should include the data cutoff date.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
