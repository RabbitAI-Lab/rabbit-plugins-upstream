## Description:

Review supplied US patent application claims and relevant specification, drawings, Office-action, and prosecution context for claim quality, prosecution readiness, 35 U.S.C. 101/102/103/112 risk, BRI, 112(f), dependency/form, restriction/election, continuation/divisional strategy, infringement observability, and amendment options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External patent teams, patent practitioners, and IP operations users use this skill to review supplied US patent claims and prosecution materials for drafting quality, statutory risk, amendment options, and structured issue records. It supports drafting and review assistance, not legal advice or filing decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent applications, prosecution records, and commercial embodiment details may contain sensitive or privileged information.

Mitigation: Use appropriate confidentiality controls before sharing materials with an agent or optional connector, and limit inputs to the review scope.

Risk: Optional PatSnap connectors can perform external patent lookup or search when requested.

Mitigation: Use connectors only when external retrieval or search is intended, keep API keys secret, and record search status, queries, dates, and authorities in the output.

Risk: The skill can produce drafting suggestions and amendment language that may affect filing rights, new matter, deadlines, or legal positions.

Mitigation: Treat outputs as review assistance and route filing decisions, deadlines, inventorship, new matter, infringement, enforceability, and legal opinions to qualified US patent counsel.

Risk: Claims-only reviews can leave support, enablement, 112(f), prosecution history, and amendment-basis conclusions preliminary.

Mitigation: Require the output to identify missing materials, state uncertainty, and avoid final conclusions when the specification, drawings, filing history, cited art, or docket information is unavailable.

## Reference(s):

- [US Patent Claims Review Checklist](references/review-checklist.md)
- [PatSnap Patent Briefing MCP Marketplace](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap Advanced Patent Search MCP Marketplace](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [USPTO Subject-Matter Eligibility](https://www.uspto.gov/patents/laws/examination-policy/subject-matter-eligibility)
- [MPEP 2106: Patent Subject Matter Eligibility](https://www.uspto.gov/web/offices/pac/mpep/s2106.html)
- [MPEP 2111: Broadest Reasonable Interpretation](https://www.uspto.gov/web/offices/pac/mpep/s2111.html)
- [MPEP 2181: 35 U.S.C. 112(f)](https://www.uspto.gov/web/offices/pac/mpep/s2181.html)
- [MPEP 608.01(n): Dependent and Multiple Dependent Claims](https://www.uspto.gov/web/offices/pac/mpep/s608.html)
- [MPEP 802: Restriction Practice](https://www.uspto.gov/web/offices/pac/mpep/s802.html)
- [MPEP 823: PCT/371 Unity Distinction](https://www.uspto.gov/web/offices/pac/mpep/s823.html)
- [PatSnap Developer Center](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with tables, issue records, claim-by-claim analysis, and amendment guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should identify document scope, search status, support locators, uncertainty, missing materials, and qualified-counsel review gates.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
