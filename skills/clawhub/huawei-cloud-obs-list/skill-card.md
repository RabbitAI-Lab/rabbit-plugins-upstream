## Description:

Lists Huawei Cloud OBS buckets and returns a table, JSON array, or bucket-name list for inventory workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inventory buckets in a Huawei Cloud OBS account and pass the results to reviews or downstream automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags execution overrides as outside the read-only safeguards and says the SDK fallback ignores the requested endpoint and result limit.

Mitigation: Use only trusted or restricted execution overrides. Verify the endpoint and result scope when the SDK fallback runs, use listing-only credentials, and verify the CLI installation source.

## Reference(s):

- [KooCLI installation guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [CLI installation and credential guide](artifact/references/cli-installation-guide.md)
- [Least-privilege IAM policy](artifact/references/iam-policies.md)
- [Verification method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Aligned text table, JSON array, or bucket-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bucket listing only; results are capped by page size.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
