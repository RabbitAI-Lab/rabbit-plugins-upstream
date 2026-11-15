## Description:

Analyzes post-feeding fish video to report feeding activity indicators and retrieve historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and aquaculture operators can submit post-feeding fish video for an activity report and retrieve prior reports. The report is intended as a visual activity assessment, not a disease diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the release suspicious with medium confidence and recommends DO_NOT_INSTALL, citing undeclared account and credential handling, privacy-relevant video uploads, and behavior that may not match the advertised analysis.

Mitigation: Do not install until the publisher explains account and credential handling, the analysis behavior, and whether export-only mode avoids analysis.

Risk: Video uploads may expose private aquarium or facility footage; the scan guidance says the upload destination and consent process need clarification.

Mitigation: Confirm the upload destination, retention and sharing practices, and obtain appropriate consent before submitting footage.

Risk: The security scan is partial because one local reference was unresolved, so it does not establish that every referenced component was reviewed.

Mitigation: Resolve and review the missing reference and its behavior before considering installation.

## Reference(s):

- [API interface and input guidance](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-fish-feeding-activity-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured feeding activity reports and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include a 0–100 activity score, observed feeding indicators, and suggested follow-up; the skill documentation prohibits disease diagnoses and medication advice.]

## Skill Version(s):

1.0.20 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
