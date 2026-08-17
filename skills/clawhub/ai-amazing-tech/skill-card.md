## Description:

Routes technology and patent-intelligence requests to technology landscape analysis, patent mining, or technology intelligence brief workflows that generate unified HTML reports using PatSnap patent and research data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, IPR teams, R&D engineers, and strategy decision makers use this skill to generate patent landscape, patent mining, and technology intelligence HTML reports for a technology domain, company, competitor set, or patent search query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill may send technology domain, company, competitor, and strategy context to PatSnap MCP or web-search services.

Mitigation: Confirm the user and organization are comfortable granting those tool permissions and sharing that context before installation or use.

Risk: Generated patent, legal, news, policy, and research analysis can be incomplete, outdated, or unsuitable as final advice.

Mitigation: Treat reports as analysis support and verify cited patents, news, policies, and other sources before relying on them.

Risk: Without PatSnap MCP account authorization and enabled search tools, the skill cannot retrieve live patent or intelligence data.

Mitigation: Complete PatSnap Open Platform setup and MCP authorization before expecting database-grounded reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/ai-amazing-tech)
- [Reference UI template](artifact/references/reference_ui_template.html)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [HTML reports with embedded CSS and JavaScript, plus concise conversational checkpoints and setup guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PatSnap MCP authorization and enabled patent-search or web-search tools for live data. Reports should show matched_total patent counts and source labels.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
