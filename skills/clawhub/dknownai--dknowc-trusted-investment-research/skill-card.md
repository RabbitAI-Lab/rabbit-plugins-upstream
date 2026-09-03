## Description:

This skill generates traceable listed-company research reports that combine public financial data with DKnowC policy and standards retrieval, including policy impact analysis, valuation scenarios, and research-only decision matrices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to research A-share listed companies, inspect financial metrics and industry context, and assess policy or standards impacts with cited sources and non-advisory valuation framing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated valuation bands and action labels could be mistaken for trading instructions.

Mitigation: Treat the report as research support only, verify cited financial and policy sources, and do not rely on it as investment advice.

Risk: The skill can install akshare into the active Python environment and contact DKnowC and public finance-data services.

Mitigation: Deploy in an approved environment, review network access, and confirm package installation behavior before use.

Risk: Optional policy-search setup may involve phone/SMS verification and a DKNOWC_API_KEY.

Mitigation: Use approved credential handling, avoid exposing the full key in chat or logs, and store the key through the runtime's secret mechanism.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknowc-trusted-investment-research)
- [DKnowC open platform](https://open.dknowc.cn/)
- [DKnowC platform](https://platform.dknowc.cn/)
- [DKnowC dependable search](https://open.dknowc.cn/dependable/search)
- [Sample BYD report](reference/比亚迪_报告.md)
- [Sample Xingtong report](reference/兴通股份_报告.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report, traceable HTML report, and JSON data snapshot, with setup commands when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research reference only; not investment advice. Policy and standards retrieval requires DKNOWC_API_KEY, while public financial data can run without that key.]

## Skill Version(s):

1.1.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
