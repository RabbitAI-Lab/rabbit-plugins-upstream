## Description:

Innovation Radar helps R&D teams identify potential technical innovations from reports, meeting notes, technical proposals, and experiment records, then triage protection options, value ratings, and follow-up questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

R&D teams, IP engineers, and technical leaders use this skill to screen everyday R&D materials for potentially protectable inventions before formal patent drafting or legal review. It produces an initial triage report with candidate innovation points, protection-path suggestions, value ratings, patent-search evidence when configured, and targeted follow-up questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: R&D notes and technical plans may contain confidential IP or trade-secret material.

Mitigation: Confirm organizational approval before submitting sensitive content to the configured PatSnap/Zhihuiya MCP service.

Risk: The generated report is preliminary IP triage and may be mistaken for legal advice or a patentability opinion.

Mitigation: Require review by qualified IP professionals before filing, disclosure, protection, or abandonment decisions.

Risk: HTML reports assembled from untrusted pasted content can expose users to unsafe markup if content is not escaped.

Mitigation: Escape user-provided content before writing HTML and avoid opening reports generated from untrusted raw HTML.

Risk: Patent-search evidence depends on MCP availability, authorization, and quick-screen retrieval settings.

Mitigation: Verify MCP configuration before relying on search-backed conclusions and perform deeper novelty review for high-value candidates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/innovation-radar)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [Innovation extraction standard](artifact/references/innovation_extraction_prompt.md)
- [Innovation taxonomy](artifact/references/innovation_taxonomy.md)
- [Patentability criteria](artifact/references/patentability_criteria.md)
- [Protection decision tree](artifact/references/protection_decision.md)
- [Follow-up question bank](artifact/references/followup_questions.md)
- [MCP usage guide](artifact/references/mcp_usage_guide.md)
- [HTML report template](artifact/references/html_template.md)

## Skill Output:

**Output Type(s):** [Files, Guidance, Text]

**Output Format:** [HTML report with structured tables, action queue, innovation details, patent-search evidence, and follow-up questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call configured PatSnap/Zhihuiya MCP patent-search tools for novelty screening when technical elements are complete.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
