## Description:

Analyzes fixed-camera video from early education settings to summarize children's social interactions and produce reports and heatmaps for educators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and early childhood educators can review interaction patterns, counts, and durations from classroom or play-area video to inform day-to-day support. The reports are observational aids and do not provide a clinical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may still upload children's videos to a remote service, and server-side privacy and retention practices are unverified.

Mitigation: Use synthetic footage in an isolated workspace for evaluation. Before using real footage, resolve the no-analysis behavior and confirm processing, retention and deletion terms, charges, authorization, and guardian and institutional consent.

Risk: Credential handling and automatic HTTP logging have concrete security weaknesses; account creation may also occur automatically.

Mitigation: Require destination-bound credentials, address HTTP logging, and confirm account-creation behavior before use with real footage. Do not rely on --api-url or --export-env-only as controls until their behavior is fixed and verified.

Risk: Low-interaction flags or other video-derived observations could be mistaken for a developmental or autism diagnosis.

Mitigation: Treat results only as educational reference for staff and families; do not diagnose or label a child from these outputs, and seek qualified clinical evaluation when developmental concerns arise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-social-interaction-analysis-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured interaction report with summaries and report or heatmap links when returned by the service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include interaction pairs, event counts and durations, initiator statistics, low-interaction candidates, and a class-level summary.]

## Skill Version(s):

1.0.16 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
