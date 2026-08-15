## Description:

Analyzes privacy-preserving bathroom doorway or silhouette-only video to track an elder's toilet occupancy duration and issue an alert when the configured threshold, default 30 minutes, is exceeded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, nursing-home operators, and care-platform integrators use this skill to monitor toilet occupancy time from approved video sources and surface abnormal-stay alerts for human follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive bathroom-monitoring footage and occupancy reports.

Mitigation: Use only in controlled care settings with explicit informed consent, approved camera placement, and privacy-preserving capture such as doorway placement, silhouette-only detection, blur, or pixelation.

Risk: Analysis, report history, identity values, and tokens may be handled by external lifeemergence cloud services and local SQLite storage.

Mitigation: Review cloud service use, token handling, retention, and local storage controls before installation; restrict access to trusted operators and approved environments.

Risk: The skill emits safety alerts and suggestions but is not a medical diagnosis or emergency-response system.

Mitigation: Treat alerts as prompts for human verification and maintain a separate emergency response plan for elder care incidents.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-elderly-toilet-time-abnormal-analysis)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [JSON or Markdown text containing structured monitoring results, alert status, suggestions, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report text to a local file when an output path is provided.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
