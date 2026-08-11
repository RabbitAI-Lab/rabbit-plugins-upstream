## Description:

Triggers when a user provides a video of a pet feeding bowl area for analysis; supports local video uploads or network URLs to call server-side APIs for picky-eater behavior detection, identifying behaviors such as pushing kibble out of the bowl, picking only treats/freeze-dried bites, or sniffing then leaving without eating; records frequency and outputs feeding-adjustment suggestions to prevent malnutrition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet feeding-bowl videos or video URLs for selective refusal behaviors and receive structured feeding-behavior reports. It is intended for smart pet feeders, pet boarding centers, and pet hospital inpatient settings as behavioral feeding guidance, not disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet videos or video URLs to a remote service for analysis.

Mitigation: Use only with approved content and consent, verify the configured service endpoint, and confirm data-handling requirements before deployment.

Risk: The skill may silently create or reuse a service identity, query prior reports, and store returned tokens in a local workspace database.

Mitigation: Deploy only where account linkage and local token persistence are acceptable; isolate the workspace and clear local stored credentials or reports according to environment policy.

Risk: The output is feeding-behavior guidance and is not a medical diagnosis.

Mitigation: Present results as observational feeding guidance and route persistent appetite, nutrition, or health concerns to qualified veterinary review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-picky-eater-detection-analysis)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with report links and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can analyze a local video file or network video URL, list historical reports, and save output when an output path is provided.]

## Skill Version(s):

1.0.6 (source: server release metadata; SKILL.md frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
