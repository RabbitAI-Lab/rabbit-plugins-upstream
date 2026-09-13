## Description:

Searches, lists, and helps install Huawei Cloud agent skills by querying public Huawei Cloud skill indexes with keyword and category filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to discover Huawei Cloud-related agent skills, inspect relevant matches, and receive installation guidance for a selected skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes outbound requests to Huawei Cloud endpoints and can send automatic quality telemetry.

Mitigation: Use it only in environments where those outbound requests are acceptable, and set SKILL_QUALITY_DISABLE=1 for local use when telemetry should be disabled.

Risk: The installation flow can add additional remote skills without pinning a reviewed source version.

Mitigation: Review the selected skill source and version before installing or executing it.

Risk: Ambient Huawei Cloud AK/SK credentials could increase exposure if present in the agent runtime.

Mitigation: Run the skill without ambient Huawei Cloud AK/SK credentials unless they are explicitly required for a separately reviewed workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-find-skills)
- [IAM Policies](artifact/references/iam-policies.md)
- [Verification Method](artifact/references/verification-method.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Huawei Cloud skills index](https://gitcode.com/api/v5/repos/2501_91318609/skills-for-index/contents/skills-index/index.json?ref=main)
- [Huawei Cloud Chinese-English keyword map](https://gitcode.com/api/v5/repos/2501_91318609/skills-for-index/contents/skills-index/cn-en-map.json?ref=main)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and search-result text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include matched skill names, categories, services, descriptions, triggers, fallback suggestions, and installation commands.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
