## Description:

Submits sandbox and ECS deployment links to Huawei Cloud’s Open Capabilities Challenge and reports the awarded points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers participating in the Huawei Cloud Open Capabilities Challenge use this skill to submit sandbox and ECS deployment links for the corresponding milestones and receive submission status and points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cleanup instructions authorize cloud-resource deletion beyond the access described elsewhere.

Mitigation: Do not proceed with cleanup until the user confirms the exact resource IDs and deletion effects; decline if the scope is unclear.

Risk: Submission uses account credentials, and optional gallery publishing can expose selected project files.

Mitigation: Use limited, short-lived credentials and do not print credential values. Before gallery publishing, review the skill, pin its version, and check that selected files contain no secrets or unrelated content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-activity-submit)
- [Verification method](artifact/references/verification-method.md)
- [Credential and access guidance](artifact/references/iam-policies.md)
- [Acceptance criteria](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [API Calls, Text]

**Output Format:** [Authenticated submission requests with text status and points summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits the beginner and intermediate milestones in sequence and may ask about optional gallery publishing.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
