## Description:

Review European patent application claims and supporting application materials for EPO/EPC examination readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External patent practitioners, patent teams, and developers use this skill to review European patent application claims and supporting materials for EPC and EPO examination readiness, including clarity, support, sufficiency, added-matter, unity, novelty, inventive-step positioning, and amendment options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided patent materials may contain confidential or commercially sensitive information.

Mitigation: Install and use the skill only if you are comfortable having the agent review the materials you provide.

Risk: Optional PatSnap MCP retrieval may require authenticated service connections.

Mitigation: Use external patent retrieval only when requested, and keep API keys in service configuration rather than prompts, reports, screenshots, or source files.

Risk: Novelty and inventive-step comments can be incomplete when no external search or retrieval has been executed.

Mitigation: State whether external retrieval was executed and label search-dependent conclusions as provisional when based only on supplied materials, cited records, and user-provided prior art.

## Reference(s):

- [European Patent Claim Review on ClawHub](https://clawhub.ai/yuanzhian-patsnap/skills/review-ep-patent-claims-ip)
- [2026 EPO Guidelines for Examination](https://www.epo.org/en/legal/guidelines-epc/2026/index.html)
- [G 1/24, Official Journal 2025 A60](https://www.epo.org/en/legal/official-journal/2025/09/a60)
- [2026 EPO Guidelines F-IV 4.1: Clarity](https://www.epo.org/en/legal/guidelines-epc/2026/f_iv_4_1.html)
- [2026 EPO Guidelines F-IV 4.2: Claim Interpretation](https://www.epo.org/en/legal/guidelines-epc/2026/f_iv_4_2.html)
- [2026 EPO Guidelines F-V: Unity](https://www.epo.org/en/legal/guidelines-epc/2026/f_v.html)
- [PatSnap Open Platform Authentication Guide](https://open.patsnap.com/devportal/guides/authentication)
- [PatSnap MCP Marketplace](https://open.patsnap.com/marketplace/mcp-servers)
- [PatSnap Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with issue tables, amendment-basis tables, assumptions, and illustrative claim amendments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include provisional novelty and inventive-step analysis when external patent retrieval or prior-art search was not executed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
