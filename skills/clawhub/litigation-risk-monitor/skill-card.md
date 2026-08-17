## Description:

Monitors patent litigation risk for named assignees by combining litigated-patent discovery, INPADOC family expansion, legal-status review, case analysis, inventor trends, and report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent, legal operations, and competitive intelligence teams use this skill to monitor litigation exposure for specified target assignees and summarize related patent-family, case, geography, and inventor-trend signals. It supports risk reporting and triage, not standalone legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive target assignee names and patent-litigation queries may be sent to PatSnap and web search.

Mitigation: Use the skill only when those external queries are acceptable for the matter; avoid confidential targets unless data-sharing is approved.

Risk: Generated reports load third-party JavaScript and may include remote image fallbacks.

Mitigation: For restricted environments, bundle the JavaScript locally, disable remote image fallbacks, and review the generated report before opening or sharing it.

Risk: The skill produces litigation-risk analysis that could be mistaken for legal advice.

Mitigation: Use outputs for triage and review workflows, and have qualified counsel validate legal conclusions before action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/litigation-risk-monitor)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, code, configuration, guidance]

**Output Format:** [HTML report plus structured JSON/CSV attachments, with concise narrative analysis and risk conclusions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a target assignee list; may query PatSnap and web search; generated reports may load third-party JavaScript unless bundled locally.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
