## Description:

Analyzes cat climbing frame or cat tree videos from local files or URLs to generate structured activity reports with dwell time by area, jump or transition counts, activity-density observations, and 2D heatmap results without providing medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet behavior monitors, caregivers, and developers use this skill to turn fixed-camera cat tree footage into structured activity summaries and heatmap-style observations for enrichment and exercise review. It is intended for observational analysis, not disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to the service backend for analysis.

Mitigation: Avoid private camera feeds, household-sensitive recordings, or internal network URLs unless the publisher clarifies endpoint handling, retention, and deletion behavior.

Risk: The skill silently creates or reuses an internal user identity and sends identity data to the backend.

Mitigation: Run only in environments where this account association behavior is acceptable and review account creation and cleanup expectations before deployment.

Risk: Service tokens may be stored in a local workspace database.

Mitigation: Protect the workspace, avoid sharing generated local data stores, and remove local state after use when the environment requires tighter data handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-climbing-frame-heatmap-analysis)
- [Pet climbing frame API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with report links when returned by the service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dwell-time summaries, transition counts, activity-density observations, heatmap results, recommendations, and historical report tables.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
