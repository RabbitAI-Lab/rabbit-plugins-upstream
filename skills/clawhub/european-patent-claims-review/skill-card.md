## Description:

Reviews European patent application claims for EPC/EPO readiness and returns structured Chinese-language findings, risk ratings, and amendment options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent attorneys, patent engineers, and IP teams use this skill to review uploaded or referenced European patent claims, specifications, PCT/EP national phase drafts, or Chinese patent text intended for Europe against EPC/EPO practice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpublished patent drafts or business-sensitive claim text may be sent to configured PatSnap MCP services during database-supported analysis.

Mitigation: Confirm organizational policy and provider account/data-handling terms before submitting confidential patent material.

Risk: Without configured PatSnap MCP services or prior-art inputs, the skill cannot provide database-supported conclusions or a complete patentability search.

Mitigation: Use its framework-only analysis mode, provide closest prior art or search opinions, and verify novelty and inventive-step conclusions before relying on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/european-patent-claims-review)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [PatSnap MCP Server Marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [PatSnap Authentication Guide](https://open.zhihuiya.com/devportal/guides/authentication)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Chinese Markdown with tables and structured review sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an overall readiness rating, issue table, detailed EPC/EPO analysis, amendment options, specification follow-up edits, and missing-input notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
