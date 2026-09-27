## Description:

Analyzes tomato and chili plant images or videos to estimate flower counts, young-fruit counts, and fruit-set rate through a cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and developers use this skill to assess flowering and fruit set in tomato or chili crops from plant imagery and review cloud-hosted analysis reports and history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media or supplied URLs are sent to an external cloud service.

Mitigation: Review the publisher's privacy and retention terms and avoid uploading sensitive media.

Risk: The skill may create or reuse an account identity, store tokens locally, and query cloud report history.

Mitigation: Clarify identity and token handling before use, especially in shared workspaces.

Risk: Some bundled code and API documentation still refer to unrelated pet-health workflows.

Mitigation: Check returned reports and links against the intended plant-analysis task before relying on them.

## Reference(s):

- [Publisher-provided API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and an optional saved result file]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; bundled frontmatter states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
