## Description:

Analyzes succulent plant images or videos to detect black rot, leaf melting, and stretching, then returns the detected condition, severity, confidence, and report link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to submit succulent plant media for cloud-based special-state detection and retrieve structured findings or historical reports. It is intended for home care, greenhouse, and flower-shop workflows where early visual identification of black rot, melting, or stretching is useful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or remote media URLs are sent to a cloud analysis service.

Mitigation: Use the skill only with media that is acceptable to share with the service, and avoid submitting private or sensitive imagery.

Risk: The skill can create or reuse an account-linked identity and store user records or service tokens locally.

Mitigation: Review and protect the workspace data directory, and rotate or remove stored tokens when the skill is no longer needed.

Risk: History and report features query cloud-stored analysis records.

Mitigation: Use history queries only when retrieving cloud-stored reports is expected, and verify that returned records belong to the intended account context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance]

**Output Format:** [Markdown report with structured JSON content and optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity, confidence, detected condition, history entries, and report export links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
