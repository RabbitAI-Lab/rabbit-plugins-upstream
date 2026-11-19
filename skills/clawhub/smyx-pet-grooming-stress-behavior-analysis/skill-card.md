## Description:

Analyzes pet grooming videos for stress-related behaviors and produces an observational stress-level report to help care providers respond during grooming.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet groomers, veterinary teams, and pet-care providers can use the skill to review grooming-session videos for stress-related behaviors and receive a structured report to support timely care decisions. Reports are for behavioral observation and do not diagnose health conditions or prescribe behavior modification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that video media may be submitted to a remote service for analysis.

Mitigation: Send only footage you are authorized to share, remove unnecessary personal details, and confirm the destination before submitting a video.

Risk: The security review reports identity and credential handling, along with profile and analysis-history features.

Mitigation: Use only necessary, access-limited credentials and review how identity details and stored reports are managed before using the service with sensitive footage.

Risk: The security review warns that a no-analysis option may still submit media.

Mitigation: Do not rely on that option to keep a video local; verify its behavior first and avoid using it with footage that must remain private.

Risk: ClawScan reports partial coverage because a referenced local path was missing, leaving the security evidence incomplete.

Mitigation: Review the available skill files and media-submission settings before installation; treat the scan verdict as a warning with incomplete coverage.

## Reference(s):

- [Skill page on ClawHub](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Guidance]

**Output Format:** [Structured report with observed behavior signals, a stress-level assessment, and report links; JSON or Markdown depending on the requested detail.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Observational guidance only; no medical diagnosis or behavior-modification plan.]

## Skill Version(s):

1.0.18 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
