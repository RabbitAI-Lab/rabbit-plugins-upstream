## Description:

Generates inventor departure monitoring briefs by identifying potentially departed inventors, checking recent patent activity at other organizations, comparing technical similarity, and producing structured HTML risk alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

IP, legal, and patent intelligence teams use this skill to monitor inventors who may have left a target company and to triage whether their recent patent filings elsewhere overlap with the company's technical domains. It can work from a company plus technology keywords or from directly supplied inventor names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, inventor names, and technical keywords are used for patent searches through the configured PatSnap MCP service.

Mitigation: Confirm the PatSnap MCP service is trusted, authorized, and configured before running live searches.

Risk: Same-name inventors can create false positive matches.

Mitigation: Review high-risk and medium-risk results manually using IPC classes, technical terms, assignees, and patent details before acting.

Risk: Patent publication delays can hide recent applications and make current risk appear lower than it is.

Mitigation: Use rolling monitoring and treat the most recent 18 months as potentially incomplete.

Risk: Generated HTML reports may contain sensitive monitoring conclusions.

Mitigation: Handle report files as local artifacts and share them only with the intended IP, legal, or patent intelligence reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/inventor-resignation-monitor)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [Inventor resignation monitor workflow](artifact/references/workflow.md)
- [Inventor monitor data schema](artifact/references/data_schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Analysis prompt text, command examples, structured JSON input, and local HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include risk levels, patent comparison tables, and suggested follow-up actions.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
