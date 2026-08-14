## Description:

Review claims in a Korean patent application or a foreign or PCT application intended for Korea, producing evidence-backed assessment of claim compliance, claim architecture, scope strategy, drafting and translation quality, examination risk, novelty or inventive-step risk, amendment options, or filing readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External patent teams, IP analysts, and drafting reviewers use this skill to pre-review Korean patent claim sets and related records before counsel review, filing, amendment, or prosecution strategy decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reviews sensitive patent documents and may use configured PatSnap connectors.

Mitigation: Use it only with patent records and connector access that the deploying organization is comfortable exposing to the agent.

Risk: Patent review output could be mistaken for legal advice or final Korean filing guidance.

Mitigation: Treat the output as structured pre-review and require qualified Korean patent counsel to review filing decisions and final claim language.

Risk: Text-only review cannot support novelty, inventive-step, or invalidation conclusions without actual prior-art retrieval.

Mitigation: Require real searches, source locators, and search logs before assigning substantive prior-art risk ratings.

## Reference(s):

- [KIPO Patent Examination Guidelines](https://www.kipo.go.kr/en/HtmlApp?c=92006&catmenu=ek03_06_01)
- [KIPO February 2026 English Patent Examination Guidelines](https://www.kipo.go.kr/upload/en/download/Patent%20Examination%20Guidelines_February%202026.pdf)
- [KIPO Intellectual Property Laws and Regulations](https://www.kipo.go.kr/en/HtmlApp?c=92005&catmenu=ek03_05_01)
- [KIPO Patent Application Procedure](https://www.kipo.go.kr/en/HtmlApp?c=30101)
- [PatSnap Advanced Patent Search MCP Server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP Server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured English report, or a complete portable HTML report when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes claim inventories, issue findings, evidence ledgers, search logs, amendment options, prioritized action registers, limitations, and counsel sign-off points.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
