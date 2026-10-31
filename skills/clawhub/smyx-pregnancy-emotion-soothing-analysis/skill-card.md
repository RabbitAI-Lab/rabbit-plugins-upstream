## Description:

Analyzes video and optional audio from a pregnant person's home or prenatal waiting room for possible signs of emotional distress and can trigger soothing actions or caregiver alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pregnant people and their caregivers use this skill to review possible emotional distress signals in provided video and optional audio, receive a structured report, and trigger soothing actions or a caregiver alert. The skill describes behavioral signals and does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive audio and video may be uploaded even when export-only behavior is expected.

Mitigation: Before using real recordings, confirm cloud processing, the destination service, and consent from everyone recorded; do not rely on export-only behavior without verification.

Risk: Account credentials may be handled unsafely.

Mitigation: Restrict credential destinations and keep secrets separate from account identifiers.

Risk: Retention, deletion, and account ownership behavior at the remote service is unverified.

Mitigation: Confirm account ownership and retention/deletion practices with the service before sending recordings, and do not rely on an advertised deletion limit without verification.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Structured analysis, Guidance, Markdown]

**Output Format:** [Structured report (JSON or text); history can be presented as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report link; results can be saved to a file.]

## Skill Version(s):

1.0.15 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
