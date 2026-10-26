## Description:

Counts immediate or nested directories in a Huawei Cloud OBS bucket or prefix and returns a numeric count without modifying resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to count OBS directories under a bucket or prefix for inventory and structure checks. It does not count files or objects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manually installed Huawei CLI tools may come from an unverified download.

Mitigation: Verify the download source is official and prefer checksum-verified or package-manager installation where available.

Risk: OBS credentials may be exposed or grant broader access than directory listing requires.

Mitigation: Use credentials limited to listing the needed bucket; do not paste access keys into chat and protect the local obsutil configuration file.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Single integer as plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Counts immediate or recursive directories, not objects; errors return guidance instead of a count.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
