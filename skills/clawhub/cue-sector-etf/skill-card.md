## Description:

This skill helps users analyze A-share sector themes and ETFs through sector overviews, ETF comparisons, holding look-through, valuation context, and risk notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ETF investors, advisors, and agents use this skill to request structured research on A-share sector themes and related ETFs, including comparisons, holdings exposure, valuation context, and risk notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or updates external runner code before use.

Mitigation: Review the Cue/sensedeal runner source before installation or update, and install it only from a trusted source.

Risk: The skill sends API-key-authenticated ETF research prompts to cuecue.cn.

Mitigation: Use a scoped or easily rotated Cue API key, avoid including private account balances or proprietary strategy details, and rotate the key if exposure is suspected.

Risk: The skill produces investment research that may depend on external data freshness and service availability.

Mitigation: Treat reports as research support rather than trading advice, verify material ETF data against issuer or exchange sources, and review risk notes before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-sector-etf)
- [Cue service](https://cuecue.cn)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue runner source referenced by skill documentation](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by skill documentation](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research report with tables, source links, setup commands, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Cue API key; research quality and freshness depend on Cue service availability and public ETF data sources.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
