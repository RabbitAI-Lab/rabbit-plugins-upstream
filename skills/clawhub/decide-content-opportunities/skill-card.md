## Description:

Generates evidence-constrained keyword and content-opportunity decisions through the SignalDig Decision MCP, including a traceable stance, qualitative confidence, counter-evidence, conditions, risks, and a next validation test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and content strategists use this skill to decide whether and how to prioritize a keyword opportunity for a specific domain, market, language, audience, and business goal. It supports bounded recommendations from SignalDig evidence rather than finished content, publishing, or final business approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill cannot produce valid decisions unless the SignalDig Decision MCP server and API key are configured separately.

Mitigation: Verify that submit_keyword_decision_report and get_keyword_decision_report are available before starting, and stop rather than simulate results when the tools are missing.

Risk: SignalDig requests may include keyword, domain, market, language, audience, and business context.

Mitigation: Review the context before submitting a request and avoid sending sensitive information that should not be shared with the external service.

Risk: API keys can be exposed if placed in shared repositories or public skill files.

Mitigation: Store the SignalDig API key only in the AI client's MCP configuration or secret store, and never commit it to the skill artifact.

## Reference(s):

- [SignalDig](https://signaldig.com/)
- [SignalDig Decision MCP Endpoint](https://mcp.signaldig.com/signals/seo/mcp)
- [Setup Guide](references/setup-guide.md)
- [Decision MCP Functional Contract](references/mcp-contract.md)
- [Evidence Evaluation](references/evidence-evaluation.md)
- [Qualitative Confidence Rubric](references/confidence-rubric.md)
- [Content Opportunity Decision Template](references/content-decision-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown decision report with recommendation, evidence basis, qualitative confidence, risks, next test, and source job trace]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured SignalDig Decision MCP server and API key; decision claims must cite real tool results.]

## Skill Version(s):

1.3.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
