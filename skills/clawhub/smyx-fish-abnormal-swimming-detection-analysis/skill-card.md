## Description:

Analyzes aquarium footage for unusual fish swimming postures and presents cloud-generated findings, alerts, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and monitoring operators use this skill to submit fish footage, review unusual swimming activity and historical reports, and decide when to inspect tank conditions or seek professional advice. The findings are not a disease diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish footage or video URLs are sent to LifeEmergence cloud services, potentially exposing sensitive camera content.

Mitigation: Use only footage you are authorized to share; check the service's handling and retention terms before submitting sensitive recordings.

Risk: The skill silently creates or reuses an identity and persists tokens in the workspace data directory.

Mitigation: Review the skill before installation and restrict access to the workspace data directory and stored credentials.

Risk: Automatic cloud-history retrieval can expose reports associated with the local identity.

Mitigation: Limit workspace access to trusted users and review who can request historical reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis)
- [Fish swimming analysis API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured analysis text or JSON with findings, suggestions, and report links; historical reports as a list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can print results or save them to a file.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
