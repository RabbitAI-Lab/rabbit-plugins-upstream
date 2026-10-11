## Description:

Analyzes rose images or videos for common pests and diseases, estimates severity, and offers general care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners and rose growers use the skill to assess images or videos of leaves, shoots, and buds for common pests and diseases, then review severity and general care suggestions. They can also request account-linked historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rose images, videos, or media URLs may be sent to an external cloud service.

Mitigation: Avoid sensitive media and confirm cloud processing is acceptable before submitting files or URLs.

Risk: The skill silently creates or reuses an account identity and stores session tokens locally.

Mitigation: Review local credential storage and restrict access to the workspace data directory.

Risk: Historical report queries can access account-linked records beyond the current diagnosis.

Mitigation: Only query reports for an account you are authorized to use and review the returned records before sharing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-rose-pest-disease-detection-analysis)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Text or Markdown report; optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pest or disease identification, severity, general care suggestions, and report links; historical reports can be presented as a Markdown table.]

## Skill Version(s):

1.0.8 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
