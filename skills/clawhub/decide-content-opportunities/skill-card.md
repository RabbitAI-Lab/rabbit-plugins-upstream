## Description:

Evaluate content opportunities from SignalDig search data to support topic selection and prioritization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT

## Use Case:

External content, SEO, and growth teams use this skill to request evidence-constrained keyword and content opportunity decisions from SignalDig's Decision MCP, including a stance, qualitative confidence, counter-evidence, conditions, risks, and a next validation test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the AI client to SignalDig's MCP endpoint can expose a SignalDig API key if credentials are stored unsafely.

Mitigation: Use environment variables or the client's secret store, avoid committing MCP configuration with credentials, and keep tool approval prompts enabled for live MCP calls.

Risk: The skill can mislead users if recommendations are fabricated when the MCP server is unavailable or evidence gaps are ignored.

Mitigation: Stop when the MCP tools are unavailable, rely only on real tool results, cite request IDs and evidence IDs, and disclose limitations or missing evidence.

Risk: Content opportunity recommendations can be mistaken for guaranteed business outcomes or final business decisions.

Mitigation: Use qualitative confidence, keep the decision owner human, and validate material recommendations with the next test and stop conditions before costly action.

## Reference(s):

- [SignalDig homepage](https://signaldig.com/)
- [Content Opportunity Decisions on ClawHub](https://clawhub.ai/jerrykik/skills/decide-content-opportunities)
- [Setup Guide](references/setup-guide.md)
- [Decision MCP Functional Contract](references/mcp-contract.md)
- [Evidence Evaluation](references/evidence-evaluation.md)
- [Qualitative Confidence Rubric](references/confidence-rubric.md)
- [Content Opportunity Decision Template](references/content-decision-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown response with traceable decision sections and optional decision-template fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live Decision MCP results; SEO claims should cite request_id and evidence_id.]

## Skill Version(s):

1.5.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
