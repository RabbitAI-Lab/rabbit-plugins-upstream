## Description:

Utilizes vision and radar technology for contactless detection of falls, triggers alarms within seconds, and supports home safety monitoring for elderly people living alone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, home-care operators, and agents use this skill to analyze uploaded monitoring images, videos, or media URLs for possible elderly falls and to retrieve prior fall-detection reports. Results are safety-alert guidance and should be confirmed by a responsible person before action is taken.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home-monitoring images, videos, or URLs may be sent to lifeemergence.com cloud services for analysis.

Mitigation: Use only with appropriate consent, privacy controls, retention rules, and approval for third-party cloud processing.

Risk: The skill may create or reuse an internal identity and persist account tokens in the workspace data directory.

Mitigation: Run it in a governed workspace, restrict access to local data files, and rotate or remove stored tokens when no longer needed.

Risk: Fall-detection results are safety alerts and may be incomplete or incorrect.

Mitigation: Require human confirmation and established emergency-response procedures before relying on an alarm.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-fall-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted structured analysis, with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fall-detection findings, risk prompts, recommendations, report links, and cloud report-history records.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
