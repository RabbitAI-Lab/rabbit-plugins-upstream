## Description:

Queries Huawei Cloud EVS, OBS, SFS Turbo, and CBR storage resources through read-only checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud storage resources, including disks, buckets, file systems, backups, and related policies. It returns queried details for inventory and troubleshooting without changing resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup and cloud requests currently bypass certificate verification.

Mitigation: Wait until certificate verification is restored before installing dependencies or making cloud calls.

Risk: Setup validates credentials by listing IAM users, which is unnecessary for storage queries.

Mitigation: Use setup that does not require IAM user listing, with narrowly scoped, temporary read-only credentials.

Risk: Cached query results may include private cloud resource details.

Mitigation: Keep cached results private and delete them when finished.

Risk: Recycle-bin queries may prompt a separate administrative feature enablement.

Mitigation: Treat recycle-bin enablement as a separate administrative decision.

## Reference(s):

- [CBR query guide](artifact/references/cbr/guide.md)
- [EVS query guide](artifact/references/evs/guide.md)
- [OBS query guide](artifact/references/obs/guide.md)
- [SFS Turbo query guide](artifact/references/sfs/guide.md)
- [IAM permission policies](artifact/references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Readable summaries or JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only resource information; fields vary by service and query.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
