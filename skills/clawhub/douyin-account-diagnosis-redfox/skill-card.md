## Description:

Diagnoses Douyin account operating health by using RedFox account and recent-content data to produce a weighted score, risk alerts, and optimization guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, Douyin operators, MCNs, and brands use this skill to audit account health, compare competitors, and assess creator partnership risk. It returns a structured report with scores, risk warnings, supporting account data, and prioritized recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send user-provided Douyin account identifiers to RedFox for lookup and analysis.

Mitigation: Run it only when the user intentionally requests analysis of a named Douyin account, and treat generated reports as containing third-party account/profile data.

Risk: The artifact includes a built-in RedFox API key path.

Mitigation: Use a revocable user-provided REDFOX_API_KEY, avoid relying on embedded default credentials, and keep keys out of prompts, logs, code, and generated files.

Risk: Broad activation language may trigger account lookup for ambiguous account-analysis requests.

Mitigation: Confirm the target account and user intent before making the RedFox lookup when the request is ambiguous.

## Reference(s):

- [Core workflow](references/core_workflow.md)
- [Diagnosis rules](references/diagnosis_rules.md)
- [API reference](references/api_reference.md)
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFox](https://redfox.hk)
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-account-diagnosis-redfox)
- [Publisher profile](https://clawhub.ai/user/redfox-data)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown diagnostic report with tables, scores, risk alerts, account data, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires RedFox account lookup data; reports may include third-party Douyin account/profile information.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
