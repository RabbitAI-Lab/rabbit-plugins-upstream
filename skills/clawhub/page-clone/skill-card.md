## Description:

从用户提供的页面截图和描述中识别页面结构、布局尺寸、控件、按钮和可见文字，并输出用于页面复刻的结构化规格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[15926863020](https://clawhub.ai/user/15926863020)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and UI engineers use this skill to convert screenshots and written page descriptions into a detailed page replication specification before implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screenshots may contain secrets, customer data, internal URLs, financial records, or other confidential information that the skill is designed to transcribe into the page specification.

Mitigation: Crop or redact sensitive areas before use unless those values are intentionally included.

Risk: Generated page specifications may contain uncertain details when a screenshot is unclear, partially hidden, or underspecified.

Mitigation: Review the generated specification and resolve any marked uncertainties before using it for code generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/15926863020/skills/page-clone)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown structured page replication specification]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes page type, menu and tab names, layout proportions, field definitions, controls, buttons, module details, and visible text extracted from screenshots; uncertain details are marked for user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
