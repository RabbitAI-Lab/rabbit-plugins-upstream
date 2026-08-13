## Description:

Patent Research Analyst turns a technical problem and proposed solution into a PatSnap-backed patent search and analysis workflow covering technology routes, novelty checks, FTO risk, competitor tracking, recent publications, and structured HTML plus Word reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External patent, IPR, R&D, and project teams use this skill to collect invention inputs, run iterative patent searches, evaluate technology routes and novelty, assess FTO risk, track competitors, and generate structured patent analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential invention details may be sent to configured external patent research services during search and analysis.

Mitigation: Use the skill only with data the user is authorized to share with the configured PatSnap/Zhihuiya MCP services, and confirm the information card before searches proceed.

Risk: FTO and infringement analysis can be incomplete or legally sensitive if patent status, claims, or jurisdictional context are misread.

Mitigation: Treat generated FTO outputs as decision support and have qualified patent counsel review high-risk conclusions before business or legal action.

Risk: Without the required PatSnap/Zhihuiya MCP configuration, the skill cannot retrieve live patent data for evidence-backed conclusions.

Mitigation: Configure and authorize the required MCP services before relying on patent results; otherwise use the skill only to draft an analysis framework.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-research-analyst)
- [PatSnap open platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance, files]

**Output Format:** [Structured Markdown, HTML report content, and Word .docx report instructions or files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires configured PatSnap/Zhihuiya MCP services for live patent retrieval; asks for user confirmation before searching; patent numbers are expected to link to Eureka detail pages.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
