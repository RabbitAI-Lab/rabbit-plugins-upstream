## Description:

Analyzes small-molecule structures, physicochemical properties, mechanisms, synthesis routes, and R&D risks for compound dossiers, project reviews, and medicinal chemistry information preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and R&D teams use this skill to retrieve and compare compound identifiers, structures, physicochemical properties, ADMET signals, toxicity information, target interactions, and patent or literature clues. It supports single-compound reports and multi-compound comparison matrices for small-molecule research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Molecule structures, CAS numbers, SMILES strings, target questions, and project context may be sent to a third-party MCP service.

Mitigation: Review external data handling before use and avoid confidential R&D inputs unless the service has been approved for that data.

Risk: The artifact embeds a live third-party MCP endpoint with an API key.

Mitigation: Remove the embedded key, rotate it, and use approved secret management before deployment.

Risk: ADMET, toxicity, and other predicted values may be incomplete or inaccurate.

Mitigation: Label predictions clearly and require experimental validation before clinical, regulatory, or investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/small-molecule-rd-analysis)
- [Zhihuiya chemical molecule MCP endpoint](https://connect.zhihuiya.com/713886/logic-mcp?apikey=sk-3F0NsY7KOt2ZyO72XkgwUIwD80xSfBjCNKp7juA92d0HWpKu)

## Skill Output:

**Output Type(s):** [text, markdown, analysis, API calls, guidance]

**Output Format:** [Markdown reports with tables, comparison matrices, source annotations, and uncertainty notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compound data references, prediction-versus-experimental labels, and batch guidance for up to 10 compounds per query.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
