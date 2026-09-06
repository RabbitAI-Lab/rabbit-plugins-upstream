## Description:

深知可信投研 combines public China A-share financial data with DKNOWC policy and standards retrieval to produce traceable company research reports for fundamentals, policy impact, valuation context, and risk review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and agents use this skill to research China A-share listed companies, compare fundamentals, inspect policy and standards impact, and generate research-reference reports with Markdown, HTML, and JSON outputs. The skill frames valuation and decision-matrix content as research reference only, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial research, valuation ranges, or action labels may be mistaken for investment advice.

Mitigation: Keep the report disclaimer visible, treat outputs as research reference only, and verify financial data against official company filings before making decisions.

Risk: Optional DKNOWC activation can send a phone number and SMS code to DKNOWC.

Mitigation: Use activation only with explicit user consent, avoid displaying full API keys in chat, and rely on the DKNOWC_API_KEY environment variable for retrieval.

Risk: The workflow can install akshare into the active Python environment.

Mitigation: Run the provided runtime check first and perform at most one same-interpreter install when the check reports that akshare is missing.

Risk: Public financial data and policy retrieval results may be incomplete, stale, or unavailable.

Mitigation: Use the generated source links and data snapshot for review, respect the skill's degradation behavior, and avoid fabricating missing policy, standard, valuation, or percentile data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-investment-research)
- [DKNOWC open service](https://open.dknowc.cn/)
- [DKNOWC platform](https://platform.dknowc.cn/)
- [README](README.md)
- [BYD sample report](reference/比亚迪_报告.md)
- [Xingtong Shipping sample report](reference/兴通股份_报告.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report plus provenance-enabled HTML and JSON data snapshot]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional DKNOWC_API_KEY enables policy and standards retrieval; financial-data sections remain available without it.]

## Skill Version(s):

1.1.0 (source: frontmatter, release evidence, README version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
