## Description:

深知可信投研将公开披露金融数据与深知可信政策/标准检索结合，为上市公司研究生成含政策影响分析的可溯源 Markdown、HTML 和数据快照报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to research A-share listed companies, interpret fundamentals and financial metrics, and assess how policies, standards, subsidies, tax preferences, or market-access rules may affect a company or industry. Outputs are research drafts for manual review, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts DKNOWC and public finance data sources and may use a phone verification flow to provision DKNOWC access.

Mitigation: Run it only with user consent for external network access and phone verification, and avoid exposing the provisioned key in chat or committed files.

Risk: The skill may install or upgrade akshare in the active Python environment.

Mitigation: Use an isolated Python environment and run the provided runtime check before allowing dependency installation.

Risk: Generated policy-impact conclusions may contain relevance errors or be mistaken for investment advice.

Mitigation: Treat reports as research drafts, verify cited policy and financial sources manually, and keep the non-advice risk notice in generated reports.

Risk: The finance data layer may bypass local proxies for selected public finance domains.

Mitigation: Deploy in a network environment where direct access to those domains is acceptable and auditable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-investment-research)
- [Publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [artifact/README.md](artifact/README.md)
- [artifact/reference/比亚迪_报告.md](artifact/reference/比亚迪_报告.md)
- [artifact/reference/中国巨石_报告.md](artifact/reference/中国巨石_报告.md)
- [DKNOWC open platform](https://open.dknowc.cn/)
- [DKNOWC platform](https://platform.dknowc.cn/)
- [DKNOWC dependable search endpoint](https://open.dknowc.cn/dependable/search)

## Skill Output:

**Output Type(s):** [text, markdown, html, json, shell commands, configuration, guidance]

**Output Format:** [Markdown report, traceable HTML, JSON data snapshot, and agent-facing setup/run guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Policy and standards retrieval requires DKNOWC_API_KEY; finance-only research remains available without that key.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
