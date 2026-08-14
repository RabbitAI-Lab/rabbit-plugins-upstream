## Description:

ASIN Keepa curve and competitor lifecycle analysis skill for diagnosing Amazon ASIN price history, BSR, sales trends, review growth, traffic structure, lifecycle stage, and producing an HTML competitor report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce analysts use this skill to run single-ASIN competitor deep dives across Keepa, Sorftime, and SIF data. It helps assess pricing behavior, ranking movement, sales and review trends, traffic composition, lifecycle stage, and report-ready competitive findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes account login, API-key creation, payment, public upload, telemetry, and generic crawling capabilities beyond ASIN analysis.

Mitigation: Review these capabilities before deployment and install only in environments where LinkFox is trusted with ASINs, generated reports, API keys, onboarding data, and uploaded files.

Risk: Uploaded files may become public or leave the local workspace.

Mitigation: Avoid uploading confidential files and treat any uploaded report, data file, or media asset as public unless the deployment owner verifies otherwise.

Risk: Payment or credit-purchase prompts may create unexpected spend.

Mitigation: Require human review before acting on payment or credit-purchase prompts.

Risk: Gateway environment variables can redirect service calls if set to untrusted hosts.

Mitigation: Use trusted gateway endpoints only and review environment configuration before running the skill.

Risk: ASIN reports can contain incomplete, delayed, or unavailable source data.

Mitigation: Preserve data-source labels, mark missing values as unavailable, and review the generated report before making business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-asin-keepa-curve-analyst)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox guide](https://skill.linkfox.com/linkfoxskills/guide.htm)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational summaries and generated HTML report files with supporting data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long analyses are written to report files; numeric claims are expected to come from skill-returned data or Python calculations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
