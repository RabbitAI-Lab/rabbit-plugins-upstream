## Description:

Analyzes submitted nighttime bedroom or hallway videos for elderly bed-exit and wandering events and provides reports or historical report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized caregivers and care teams use the skill to request analysis of nighttime monitoring videos and review bed-exit or wandering reports and prior results. Findings require human review before care decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elder bedroom or hallway footage and video URLs are sent to a remote service.

Mitigation: Use only with consent from the monitored person or authorized representative; verify the provider's access, retention, and deletion practices before sharing footage.

Risk: Identity-linked reports and reusable service tokens may expose private care information.

Mitigation: Restrict access to report data and tokens, and review the provider's authorization controls before use.

Risk: Descriptions of continuous monitoring and alerts may exceed the demonstrated analysis workflow.

Mitigation: Do not rely on this skill as a standalone emergency or continuous safety-monitoring system; verify alerting capabilities independently and have caregivers check urgent findings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-night-bed-exit-wandering-analysis)
- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis results, report links, or Markdown report listings; JSON is available as a detail setting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file; historical report listings come from the remote service.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
