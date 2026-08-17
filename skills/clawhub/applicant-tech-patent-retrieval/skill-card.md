## Description:

Guides applicant-first patent retrieval constrained by a technology topic, including applicant/entity expansion, topic boundary validation, PatSnap/Zhihuiya query construction, deduplication, and Markdown or Word reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP teams, and agents use this skill to build auditable applicant-and-topic patent retrieval workflows for PatSnap/Zhihuiya. It is intended for searches that need both an applicant scope and an explicit technology boundary before formulas, datasets, or reports are produced.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can initiate PatSnap/Zhihuiya patent retrieval through external MCP services tied to the user's account permissions.

Mitigation: Install only when those services are intended, confirm MCP connectivity and account scope first, and treat generated datasets or reports as external-service outputs.

Risk: Incorrect applicant fields, entity expansion, or topic boundaries can create misleading patent result sets.

Mitigation: Require explicit user confirmation of the applicant field, candidate entities, topic definition, boundary table, search element matrix, and gate status before retrieval or formula finalization.

Risk: Premature formula generation can bypass review gates and produce overbroad or noisy queries.

Mitigation: Follow the visible Step 0 through Step 7 pre-retrieval validation package before any Step 8 formula or combined query output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/applicant-tech-patent-retrieval)
- [Applicant retrieval workflow](references/applicant-retrieval-workflow.md)
- [Topic limitation workflow](references/topic-limitation-workflow.md)
- [PatSnap/Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [PatSnap/Zhihuiya authentication guide](https://open.zhihuiya.com/devportal/guides/authentication)
- [PatSnap/Zhihuiya MCP server marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [PatSnap search MCP server](https://open.zhihuiya.com/marketplace/mcp-servers/patsnap-search)
- [Advanced patent search MCP server](https://open.zhihuiya.com/marketplace/mcp-servers/patent-search)
- [Patent mining MCP server](https://open.zhihuiya.com/marketplace/mcp-servers/patent-mining)
- [Patent briefing MCP server](https://open.zhihuiya.com/marketplace/mcp-servers/patent-briefing)
- [Patent visual analysis MCP server](https://open.zhihuiya.com/marketplace/mcp-servers/patent-visual)
- [Patent landscape projects MCP server](https://open.zhihuiya.com/marketplace/mcp-servers/landscape-projects)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and executable PatSnap/Zhihuiya query formulas, with optional dataset and Word-report delivery guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation of applicant field, entity scope, technology boundary, and retrieval mode before final search or report outputs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
