## Description:

Queries Huawei Cloud EVS, OBS, SFS Turbo, and CBR storage resources without modifying them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inspect Huawei Cloud disks, buckets, file systems, and backups with read-only queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe TLS settings in cloud clients could expose credentials or query data.

Mitigation: Require TLS certificate verification before use and avoid untrusted networks.

Risk: Dependency installation without pinned versions or hashes, including trusted-host bypasses, could run untrusted code.

Mitigation: Review the setup path, pin and verify dependencies, and remove trusted-host bypasses before installation.

Risk: Automatic setup and credential checks may handle sensitive cloud credentials without explicit approval.

Mitigation: Confirm setup and credential validation first; use least-privilege read-only credentials and never disclose their values.

## Reference(s):

- [EVS query guide](artifact/references/evs/guide.md)
- [OBS query guide](artifact/references/obs/guide.md)
- [SFS query guide](artifact/references/sfs/guide.md)
- [CBR query guide](artifact/references/cbr/guide.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summaries of JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only resource details; requires Huawei Cloud credentials.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
