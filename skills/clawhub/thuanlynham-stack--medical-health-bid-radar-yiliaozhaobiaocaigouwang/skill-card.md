## Description:

医疗大健康采招雷达-医疗招标采购网，当搜索词包含医院、医疗、卫生、体检时触发，重点提取采购方（医院）和中标方（医药公司/代理商），分析特定医院的Top供应商体系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Healthcare procurement researchers can search hospital bid notices, identify purchasing hospitals and winning suppliers, and review a hospital's leading supplier landscape.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic signup uses a hashed MAC address as a persistent device identifier; provider retention and server behavior are not established by the available evidence.

Mitigation: Configure your own ZLBX_API_KEY to bypass device-based signup, or proceed with signup only if you accept this device identifier use.

Risk: Version notices trigger account-linked acknowledgments after they are shown.

Mitigation: Review whether automatic acknowledgments fit your workflow before using the skill.

Risk: Some successful company and procurement lookups consume credits.

Mitigation: Limit queries to the user's requested scope and review applicable charges before using paid lookups.

Risk: Saved API keys and temporary login links could be exposed if mishandled.

Mitigation: Store keys securely and protect temporary login links; do not share secrets in conversation or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thuanlynham-stack/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Account API reference](artifact/references/api-account.md)
- [API key registration guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Concise narrative summaries and Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Procurement search and supplier analysis results; selected company lookups may consume account credits.]

## Skill Version(s):

1.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
