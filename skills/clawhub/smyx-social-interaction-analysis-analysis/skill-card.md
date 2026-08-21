## Description:

Analyzes multi-pet video or image inputs to classify social interactions, quantify duration, frequency, initiator, and receiver, and return a structured social-behavior report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, pet boarding centers, daycare staff, and behavior-clinic users can analyze multi-pet footage to understand relationships, identify possible conflict or stress patterns, and produce an observational report. The skill is for behavior observation and does not provide medical or training advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or image inputs may leave the device for remote analysis.

Mitigation: Use only footage appropriate for provider processing, and confirm retention, deletion, and access practices before submitting private household media.

Risk: The skill can create or reuse an account-linked local identity and token database.

Mitigation: Run it in an isolated workspace when possible, review generated local data, and remove identity or token files when they are no longer needed.

Risk: Cloud report history may be queried for the current workspace identity.

Mitigation: Use a dedicated identity for this skill and review or disable automatic history lookup where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-social-interaction-analysis-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance]

**Output Format:** [Markdown or JSON text with optional saved file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces structured analysis results, report links, and history-list output when requested.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
