## Description:

Helps central state-owned enterprise technology teams identify patent-backed target organizations for licensing, transfer, equity investment, or pledge-value support using Patsnap MCP and web research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Technology management, business development, and compliance teams use this skill to turn patent numbers or technology descriptions into traceable shortlists of potential internal or external counterparties. It supports path selection, three-track patent and business search, candidate scoring, and recommended next actions for technology transfer decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential patent numbers, technology descriptions, or target criteria may be sent through Patsnap MCP or web-search workflows.

Mitigation: Confirm that the user is authorized to share the task inputs with the configured tools before running searches, and record any search-boundary assumptions in the report.

Risk: Candidate recommendations may be over-trusted if patent evidence, business signals, or ownership normalization are incomplete.

Mitigation: Keep patent evidence, source timestamps, scoring rationale, risk deductions, and manual-confirmation flags visible for each recommended organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/tech-transfer-target-discovery)
- [Patsnap open platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance and generated local HTML report with optional Word and Excel/CSV exports when the runtime supports them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include source records, search timestamps, scoring rationale, candidate evidence, risk notes, and user-provided task boundaries.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
