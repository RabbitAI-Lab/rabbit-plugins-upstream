## Description:

校招/实习互联网产品经理简历评分与面试模拟技能，支持按五维评价体系评分、优化简历，并基于 JD 生成模拟面试题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[winkychannn](https://clawhub.ai/user/winkychannn)

### License/Terms of Use:

MIT-0

## Use Case:

External job candidates and career-support agents use this skill to review campus or internship product-manager resumes against a job description, identify gaps, generate a safer optimized resume draft, and prepare mock interview questions. It is aimed at Chinese-language campus PM application workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OCR mode may upload resume documents, including contact and work-history details, to Tencent Cloud under the user's credentials.

Mitigation: Use pure text input for local-only processing, or only use OCR after confirming the user accepts Tencent Cloud processing for the resume document.

Risk: Optimized resume wording can be incorrect, overstated, or unsuitable for submission.

Mitigation: Review the optimized resume before sending it to employers, especially ownership claims, quantitative placeholders, and rewritten experience descriptions.

Risk: Unused legacy helper modules may perform runtime package installation and load environment settings if invoked directly.

Mitigation: Use the documented main workflow and avoid invoking legacy helper modules unless the runtime package-install and environment-loading behavior is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/winkychannn/skills/campus-pm-coach)
- [ClawHub publisher profile](https://clawhub.ai/user/winkychannn)
- [Tencent Cloud API key console](https://console.cloud.tencent.com/cam/capi)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance, configuration]

**Output Format:** [Markdown reports and JSON scoring results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce a quick diagnostic report, scored resume report, optimized resume draft, scoring JSON, and mock interview question set.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
