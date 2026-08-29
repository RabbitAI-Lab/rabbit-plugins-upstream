## Description:

深知可信投研 combines public A-share financial data with optional DKNOWC policy and standards retrieval to produce provenance-enabled listed-company research reports with policy impact analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, researchers, and agents use this skill to research A-share listed companies, review fundamentals, compare industry context, and examine how policies, subsidies, standards, or market-access rules may affect a company or sector. The financial-data workflow remains available without a DKNOWC key, while policy and standards retrieval requires configured DKNOWC access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated investment research may be incomplete, stale, or misleading if treated as a recommendation.

Mitigation: Verify financial facts against official company filings and policy or standards claims against original source documents before relying on the report.

Risk: Policy-search onboarding may require phone verification and may create persistent DKNOWC API credentials.

Mitigation: Review and approve onboarding before registration, do not expose full keys in chat, and store access only through the DKNOWC_API_KEY environment variable.

Risk: The runtime may install or upgrade akshare in the active Python environment when the dependency is missing.

Mitigation: Run the provided runtime check first and perform the one-time install only in an approved or isolated Python environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknowc-trusted-investment-research)
- [DKNOWC Open Platform](https://open.dknowc.cn/)
- [DKNOWC dependable search](https://open.dknowc.cn/dependable/search)
- [DKNOWC platform](https://platform.dknowc.cn/)

## Skill Output:

**Output Type(s):** [Markdown, HTML, JSON, Analysis, Guidance]

**Output Format:** [Markdown report, provenance-enabled HTML report, and JSON data snapshot]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source traces for policy and standards claims when DKNOWC retrieval is configured; financial-only reports remain available without a DKNOWC key.]

## Skill Version(s):

1.0.0 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
