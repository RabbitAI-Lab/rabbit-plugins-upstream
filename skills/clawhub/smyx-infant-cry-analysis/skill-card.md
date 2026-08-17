## Description:

Detects baby cries with audio AI, analyzes likely causes such as hunger, tiredness, pain, discomfort, or irritability, and returns structured guidance for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregivers use this skill to submit infant cry audio or video for cloud-backed analysis, receive a structured report, and query previous analysis reports associated with the local identity used by the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded infant-related media and report history requests are sent to the publisher's cloud service.

Mitigation: Review the publisher's data handling, retention, and deletion controls before installing or submitting sensitive media.

Risk: The skill creates or reuses a local identity, stores session tokens in a workspace SQLite database, and attaches those credentials to future API requests.

Mitigation: Install only in a controlled workspace where this identity and token storage behavior is acceptable, and clear stored credentials when access should end.

Risk: The scanner summary notes that the media scope is broader than a narrow audio-only description.

Mitigation: Confirm the intended supported media types with the publisher and restrict uploads to expected infant cry analysis files.

Risk: The analysis is parenting support and may be incorrect or incomplete for medical situations.

Mitigation: Use outputs as reference guidance only and seek medical care when an infant shows persistent crying, discomfort, or concerning symptoms.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured analysis reports, with optional saved output files and Markdown tables for report history.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include analysis results, recommendations, report links, and cloud report-history listings.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
