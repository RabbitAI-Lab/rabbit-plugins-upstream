## Description:

Auto Lamp IP Advisor analyzes automotive lamp designs or parts lists for module breakdown, make-or-buy decisions, patent infringement risk across major jurisdictions, and interactive HTML/ZIP report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External automotive lighting product, engineering, procurement, and IP teams use this skill to assess lamp part breakdowns, source-or-make decisions, and patent risk before design or procurement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent lookups may send automotive lamp design or parts-list details to PatSnap/MCP.

Mitigation: Use only approved PatSnap accounts and workspaces, and avoid submitting confidential lamp designs unless that workspace is approved for the data.

Risk: The skill saves generated HTML and ZIP reports locally.

Mitigation: Review the generated files and storage location before sharing, retaining, or moving the report outside an approved workspace.

Risk: Patent-risk analysis may be incomplete or unsuitable as legal advice.

Mitigation: Use the output as an initial engineering and procurement aid, then obtain formal FTO review from qualified patent counsel before production decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/auto-lamp-ip-advisor)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Interactive HTML report packaged as a ZIP file, with explanatory text and patent-risk tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses PatSnap/MCP patent lookups when configured; asks for missing lamp design details before analysis.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
