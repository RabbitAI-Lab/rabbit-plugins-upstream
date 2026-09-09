## Description:

Generates evidence-constrained keyword and content opportunity decisions through the SignalDig SEO Decision MCP, including stance, qualitative confidence, counter-evidence, conditions, risks, and a next validation test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, marketers, and content teams use this skill to decide whether or how to prioritize a keyword or content opportunity from traceable SignalDig Decision MCP evidence. It is not for evidence collection alone, finished copy, publishing, or automatic business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a remote SignalDig MCP service and a valid API key; without both, it cannot produce a grounded decision.

Mitigation: Verify the required MCP tools are visible before use and stop rather than simulate recommendations when the service or credentials are unavailable.

Risk: API keys could be exposed if placed in project files, repositories, or chat.

Mitigation: Use user-level client configuration with environment variables or a secret store, and keep the SignalDig API key out of repositories and chat.

Risk: SEO recommendations may be misleading if evidence gaps, stale data, partial results, or market-language mismatches are ignored.

Mitigation: Report request IDs, evidence IDs, limitations, counter-evidence, confidence factors, and stop conditions for each decision.

## Reference(s):

- [SignalDig homepage](https://signaldig.com/)
- [SignalDig SEO Decision MCP endpoint](https://mcp.signaldig.com/signals/seo/mcp)
- [Setup Guide](references/setup-guide.md)
- [Decision MCP Functional Contract](references/mcp-contract.md)
- [Evidence Evaluation](references/evidence-evaluation.md)
- [Qualitative Confidence Rubric](references/confidence-rubric.md)
- [Content Opportunity Decision](references/content-decision-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown decision report with stance, evidence IDs, qualitative confidence, risks, conditions, next test, and source request ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live SignalDig SEO Decision MCP results and uses qualitative confidence labels only.]

## Skill Version(s):

1.5.2 (source: server release metadata, _skillhub_meta.json, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
