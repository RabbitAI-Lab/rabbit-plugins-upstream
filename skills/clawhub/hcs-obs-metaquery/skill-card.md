## Description:

Provides semantic search, scalar search, AI content-awareness setup, and bucket/object management for Huawei Cloud OBS using the OBS SDK and Huawei Cloud AI service REST APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to query Huawei Cloud OBS object metadata, run text-driven image or video lookup workflows, inspect bucket information, and prepare bucket/object management commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live execution can use Huawei Cloud credentials to read or modify OBS resources.

Mitigation: Use narrowly scoped credentials and grant write permissions only for workflows that require bucket creation or object upload.

Risk: Semantic image or video search may send OBS object references to Huawei AI services.

Mitigation: Restrict semantic search to approved buckets or prefixes and avoid sensitive media unless that processing is acceptable for the organization.

Risk: Documented IAM examples include delete permissions even though deletion should be intentional.

Mitigation: Do not grant delete permissions unless a reviewed workflow explicitly requires them.

## Reference(s):

- [IAM Permission Policies](references/iam-policies.md)
- [OBS MetaQuery API Reference](references/obs-metaquery-api.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud Image Tagging API](https://support.huaweicloud.com/api-image/image_01_0007.html)
- [Huawei Cloud VIAS API](https://support.huaweicloud.com/api-vias/vias_01_0001.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON or Markdown command output with human-readable guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mock mode can produce local validation output without cloud credentials; live mode requires Huawei Cloud credentials.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
