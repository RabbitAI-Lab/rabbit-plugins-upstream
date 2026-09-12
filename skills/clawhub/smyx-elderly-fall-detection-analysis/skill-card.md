## Description:

Uses vision and radar technology for contactless fall detection and seconds-level alarms in elderly home safety monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-technology operators use this skill to analyze monitoring images or videos for possible elderly falls, review structured detection results, and retrieve historical fall-detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive elderly-care images, videos, report queries, account identity, and stored tokens.

Mitigation: Use it with real household monitoring data only after confirming consent, secure token storage, and appropriate data-handling controls.

Risk: Media and report queries are sent to configured service endpoints.

Mitigation: Require HTTPS production endpoints and scoped destination allowlisting before deployment.

Risk: Fall-detection results are safety alerts and may be incomplete or incorrect.

Mitigation: Treat alarms as prompts for human confirmation and emergency follow-up rather than as a replacement for direct verification.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured JSON-style analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write results to a user-specified output file and supports basic, standard, and JSON detail modes.]

## Skill Version(s):

1.0.14 (source: server release metadata; SKILL.md frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
