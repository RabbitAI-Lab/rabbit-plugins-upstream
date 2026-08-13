## Description:

Real-time detection of gaze direction and facial pose to quantify states of focus, distraction, or mind-wandering for classroom learning, office meetings, and driving attention monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to submit video files or video URLs for focus analysis, receive structured attention reports, and query cloud-hosted historical reports for the internally associated identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video inputs or URLs may contain identifiable people and are sent to a remote analysis service.

Mitigation: Use only authorized footage with appropriate consent, and avoid installing the skill in private or regulated environments unless remote processing is approved.

Risk: The skill silently creates or reuses an internal identity and may store account tokens in a local workspace database.

Mitigation: Review local storage and identity persistence before deployment, restrict workspace access, and rotate or remove stored tokens when the skill is no longer needed.

Risk: The skill can query prior cloud report history associated with the resolved identity.

Mitigation: Limit access to trusted users and verify that historical report retrieval complies with privacy, retention, and authorization requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-focus-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports and structured JSON returned from command-line analysis or history queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report export link and may write the selected report output to a local file when an output path is supplied.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
