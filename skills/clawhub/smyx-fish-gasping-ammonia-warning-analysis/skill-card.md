## Description:

Analyzes fixed aquarium camera images or video for fish gasping and abnormal respiration near the water surface, producing visual hypoxia or ammonia-poisoning risk warnings and handling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarium owners, aquaculture operators, and developers use this skill to analyze clear aquarium or pond footage, receive structured gasping-risk reports, and query prior warning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary reports that media and credentials can be sent over plaintext HTTP through shipped development configuration.

Mitigation: Review configuration before installing, require production HTTPS-only endpoints, and avoid running private development endpoint settings.

Risk: The server security summary reports silent identity creation or reuse and local token storage.

Mitigation: Require explicit account binding and store tokens in a proper secrets store or keep them transient.

Risk: Cloud upload and history access may expose aquarium media or reports if account binding and retention are unclear.

Mitigation: Disclose cloud upload and history access plainly, confirm user authorization, and limit retained media to necessary warning evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON analysis reports with warning levels, recommended actions, report links, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and historical report tables when querying prior warnings.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
