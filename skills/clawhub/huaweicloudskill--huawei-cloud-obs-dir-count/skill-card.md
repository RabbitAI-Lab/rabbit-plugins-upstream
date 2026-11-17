## Description:

Count immediate or recursive directories in a Huawei Cloud OBS bucket or prefix and return the count as an integer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to count folders in a user-confirmed Huawei Cloud OBS bucket or prefix, either at one level or recursively. It returns a count and can provide JSON output or setup and troubleshooting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment says the verification runner's command filter does not guarantee commands stay within the skill's stated safety limits.

Mitigation: Avoid the runner until it is limited to fixed read-only operations; confirm test bucket names before running checks.

Risk: OBS listings use configured credentials, so excessive permissions could expose more bucket data than needed.

Mitigation: Use credentials restricted to listing the intended buckets, confirm the bucket and optional prefix before listing, and configure credentials outside chat without exposing AK/SK values.

Risk: An unverified CLI download could introduce supply-chain risk; downloaded binaries and live cloud behavior were not verified by the security assessment.

Mitigation: Obtain the CLI from Huawei's official source and verify its SHA-256 against the matching official release checksum before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-obs-dir-count)
- [Directory counting script](scripts/count_obs_directories.py)
- [CLI installation and checksum guide](references/cli-installation-guide.md)
- [Read-only IAM policies](references/iam-policies.md)
- [Troubleshooting guide](references/troubleshooting.md)
- [Huawei Cloud KooCLI download and checksum page](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud obsutil guide](https://support.huaweicloud.com/utiltg-obs/obs_11_0003.html)
- [OBS IAM authorization](https://support.huaweicloud.com/perms-cfg-obs/obs_40_0001.html)
- [Creating IAM custom policies](https://support.huaweicloud.com/usermanual-iam/iam_01_0605.html)
- [OBS bucket policy configuration](https://support.huaweicloud.com/usermanual-obs/obs_03_0123.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Integer count or JSON result, with Markdown setup and troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Counts immediate directories by default; recursive counts and a maximum depth are optional.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
