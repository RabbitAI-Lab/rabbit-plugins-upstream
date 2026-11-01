## Description:

Analyzes workplace video for facial expression and posture trends, compares them with personal baselines, and produces HR reports with employee support alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

HR teams use this skill to review workplace video trend reports and consider voluntary employee support check-ins. Use requires appropriate organizational authorization, informed employee consent, and an opt-out process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workstation coordinates and repeated behavior trends can make supposedly anonymous reports identifiable.

Mitigation: Restrict report access, minimize location detail, and do not link reports to employee names or IDs.

Risk: Workplace video and inferred emotion trends are sensitive, and video is processed by an external service.

Mitigation: Use real employee footage only with explicit authorization, informed consent, opt-out controls, transparent notice, and verified retention and access protections.

Risk: Behavioral alerts may be incomplete or misleading and could be misused in employment decisions.

Mitigation: Treat alerts only as prompts for voluntary support; do not use them for diagnosis, performance evaluation, promotion, or termination.

Risk: Stored account tokens or API secrets could expose sensitive report data.

Mitigation: Protect stored tokens and keep API secrets separate from identity fields.

## Reference(s):

- [API interface and data handling reference](artifact/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis reports, alert summaries, recommendations, and report links; JSON detail or Markdown report lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may contain anonymized subject IDs and workstation coordinates; trend analysis depends on suitable video and baseline data.]

## Skill Version(s):

1.0.13 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
