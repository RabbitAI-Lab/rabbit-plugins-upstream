## Description:

Uses Cue to generate sector and A-share ETF research, including sector overviews, ETF comparisons, holdings analysis, valuation context, and risk notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

ETF investors, advisors, and research agents use this skill to request Cue-generated analysis for A-share sectors and listed ETFs. It helps compare ETF products, inspect holdings, review valuation levels, and surface risks before independent investment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ETF and sector prompts are sent to the external Cue service using a local Cue API key.

Mitigation: Install only when external processing by Cue is acceptable, and avoid entering confidential or sensitive portfolio details in prompts.

Risk: Returned reports are externally generated financial research and may contain stale, incomplete, or misleading claims.

Mitigation: Verify the cited sources and treat the report as research input rather than personalized financial advice.

Risk: Passing external report content through verbatim can expose users to irrelevant instructions, links, or claims.

Mitigation: Ignore content unrelated to the requested ETF or sector analysis and review links and claims before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-sector-etf)
- [Cue](https://cuecue.cn)
- [Cue API key](https://cuecue.cn/hub/api-key)
- [Cue skills runner](https://github.com/sensedeal/cue-skills)
- [Cue skills runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research report with tables, risk notes, source links, and Cue runner command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports depend on Cue service availability, configured Cue API credentials, and public ETF data availability.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
