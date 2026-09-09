## Description:

Automatically identifies wet clothing and abnormal excretion via visual AI, then returns caregiver-facing reports, alerts, suggestions, and report links for care workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and care-operations users use this skill to analyze uploaded or URL-based care images and videos for damp clothing, excretion abnormalities, alert level, care warnings, and follow-up suggestions. It can also query cloud-hosted historical incontinence alert reports associated with the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send sensitive incontinence-related images, videos, report metadata, and identity-linked account data to the publisher's cloud service.

Mitigation: Use only in authorized care workflows, restrict access to approved caregivers, avoid shared workspaces, and confirm privacy and data-handling requirements before installation.

Risk: The security scan reports silent identity creation or reuse and local token storage.

Mitigation: Isolate the runtime workspace, rotate any exposed tokens, and require secure token handling before production deployment.

Risk: The security scan reports broad or plaintext network paths and arbitrary credential-forwarding concerns.

Mitigation: Require the publisher to remove plaintext HTTP and development endpoints and credential-forwarding behavior before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [智能失禁状态提醒分析 API 文档](artifact/references/api_doc.md)
- [API接口文档](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown summaries and JSON structured reports with report URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a file and may list historical cloud report records when requested.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
