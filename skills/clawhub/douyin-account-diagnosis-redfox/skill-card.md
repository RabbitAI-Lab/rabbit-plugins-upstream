## Description:

Diagnoses Douyin account operating health by retrieving RedFox account and recent content metrics, scoring six dimensions, flagging risks, and producing optimization guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

Douyin operators, creators, MCNs, brands, and business development teams use this skill to audit account health, benchmark competitors, screen creator partnerships, and prioritize account optimization work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the target Douyin nickname or ID to RedFox and reports may include profile metadata such as UID, region or IP location, demographics, and recent work metrics.

Mitigation: Install and use it only when that data sharing is acceptable, and avoid analyzing or sharing reports for accounts you are not authorized to review.

Risk: Use of a RedFox API key can tie diagnosis requests to the configured RedFox account.

Mitigation: Use a revocable REDFOX_API_KEY when you want usage tied to your own account, confirm key scope and reset options, and avoid exposing keys in prompts, logs, code, or output files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/douyin-account-diagnosis-redfox)
- [Core Workflow](references/core_workflow.md)
- [Diagnosis Rules](references/diagnosis_rules.md)
- [API Reference](references/api_reference.md)
- [RedFox API Endpoint](https://redfox.hk/story/api/dyUser/queryData)
- [RedFox API Key Settings](https://redfox.hk/settings/api-keys?source=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Structured Markdown diagnosis report with tables, risk alerts, recent content links, and prioritized recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Douyin nickname or ID as input and may include profile metadata, region or IP location, demographics, and recent work metrics returned by RedFox.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
