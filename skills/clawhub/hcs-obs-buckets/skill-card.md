## Description:

Queries Huawei Cloud OBS buckets for an account or project, with support for listing buckets, filtering by name or prefix, estimating resource-associated buckets, and listing objects in a bucket.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud OBS bucket inventory, filter buckets, check likely resource associations, and list bucket objects for operations or audit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Huawei Cloud AK/SK credentials for real OBS inventory calls.

Mitigation: Use least-privilege OBS/IAM credentials and avoid granting write or administrative permissions when inventory-only access is sufficient.

Risk: Resource-to-bucket association results are heuristic rather than an authoritative access map.

Mitigation: Treat association output as a best-effort hint and confirm access relationships against Huawei Cloud IAM, bucket policy, and ACL configuration before acting on the result.

## Reference(s):

- [Huawei Cloud OBS bucket API excerpt](artifact/obs-bucket-api.md)
- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/hcs-obs-buckets)
- [Publisher profile](https://clawhub.ai/user/yangaiwu)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Configuration guidance]

**Output Format:** [JSON or Markdown tables with command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports mock output without credentials; real calls require Huawei Cloud AK/SK credentials.]

## Skill Version(s):

0.1.1 (source: server release evidence; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
