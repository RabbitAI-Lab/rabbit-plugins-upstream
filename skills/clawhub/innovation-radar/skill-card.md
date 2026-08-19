## Description:

Innovation Radar identifies potential protectable technical innovations from R&D reports, meeting notes, technical proposals, and experiment records, then recommends protection paths, value ratings, and follow-up questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

R&D teams, IP engineers, and technical leaders use this skill to triage R&D materials, identify candidate innovations, screen novelty through a configured patent-search MCP service, and produce a shareable HTML decision report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Relevant technical details may be sent to the configured patent-search MCP provider during novelty screening.

Mitigation: Use only approved MCP accounts and workspace settings, and avoid submitting highly confidential invention details unless those data-sharing conditions are appropriate.

Risk: Generated HTML reports may contain sensitive invention details and patentability assessment context in the session workspace.

Mitigation: Store, share, and remove generated reports according to the organization's confidentiality controls.

Risk: Novelty and protection recommendations are preliminary screening outputs and may be mistaken for patent drafting, deep prior-art search, or legal advice.

Mitigation: Have an IP engineer or qualified reviewer validate findings before filing, disclosure, or protection decisions.

## Reference(s):

- [Innovation Radar Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/innovation-radar)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [Innovation Extraction and Three-Element Standard](references/innovation_extraction_prompt.md)
- [Innovation Type Taxonomy](references/innovation_taxonomy.md)
- [Patentability Criteria](references/patentability_criteria.md)
- [Protection Decision Tree](references/protection_decision.md)
- [Follow-Up Question Library](references/followup_questions.md)
- [MCP Tool Usage Guide](references/mcp_usage_guide.md)
- [HTML Report Template](references/html_template.md)

## Skill Output:

**Output Type(s):** [Files, Guidance, API Calls]

**Output Format:** [HTML report file plus a brief completion message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a configured patent-search MCP service and writes the generated report to the session workspace.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
