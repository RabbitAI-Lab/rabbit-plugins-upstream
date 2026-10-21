## Description:

企业技术专利竞争分析。当用户提到企业情报分析、竞争对手分析、竞品专利、技术竞争格局、专利布局对比、某家公司在做什么技术、行业专利态势，或要一份可交付的企业专利竞争报告时使用。常见说法：「竞品专利分析」「对手在布局什么」「某公司的专利布局」「技术情报」「专利尽调」。Use when the user asks for competitive patent intelligence, competitor technology analysis, or a company's patent landscape report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and business teams use this skill to assess a company's patent activity in a technology area, compare competitors, and prepare a decision-supporting patent landscape report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Background materials may be uploaded without clear confirmation, potentially exposing confidential information.

Mitigation: Review and approve the exact materials before upload; omit confidential content unless authorized, and consult the PatentMax privacy policy.

Risk: Reusable API credentials may be insufficiently protected.

Mitigation: Configure keys outside chat, protect the local credential directory, and request a fix for authenticated redirects before using valuable credentials.

Risk: A paid report operation may continue remotely until cancelled.

Mitigation: Confirm the paid request before submission, retain its operation ID, and cancel it if the work should stop.

## Reference(s):

- [PatentMax API Platform](https://api.ip930.com/features/api-platform)
- [PatentMax Reports API](https://api.ip930.com/api/v1/reports)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Word document]

**Output Format:** [Word (.docx) patent analysis report with concise text status and progress updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report is generated asynchronously and can be downloaded for delivery.]

## Skill Version(s):

1.1.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
