## Description:

Real-time detection of gaze direction and facial pose to quantify states of focus, distraction, or mind-wandering for classroom learning, office meetings, and driving attention monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to submit video files or URLs for focus analysis, receive structured reports, and query cloud-hosted report history. Intended scenarios include classrooms, meetings, and driving attention monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload videos or submit video URLs containing faces and behavior data to a configured cloud service.

Mitigation: Use only with authorized footage, confirm consent requirements, and verify service endpoint, retention, and access controls before deployment.

Risk: The skill can create or reuse a local identity, query cloud report history, and persist authentication tokens in a local SQLite database.

Mitigation: Review local data storage, token handling, and report authorization before use, especially in classroom, workplace, or driving contexts.

Risk: Focus-analysis results may be incomplete or misleading if treated as definitive judgments about attention.

Mitigation: Use reports as decision support only and keep human review in any consequential monitoring workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-focus-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown reports and JSON structured analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, focus scores, trend details, and saved output files when requested.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
