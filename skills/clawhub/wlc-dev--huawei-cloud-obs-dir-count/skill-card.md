## Description:

Counts the immediate or recursive directory total in a Huawei Cloud OBS bucket or prefix and returns the numeric count.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and developers use this skill to inventory directory structure in Huawei Cloud OBS buckets, check a prefix, or review nested folder counts. It reports directory counts rather than file counts or storage size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional CLI test helper can execute shell commands constructed from its inputs.

Mitigation: Avoid the helper with untrusted path or bucket values, and choose an explicit trusted test bucket.

Risk: The sample IAM policy grants listing access across OBS buckets and objects.

Mitigation: Restrict listing permissions to the intended bucket or prefix.

Risk: The setup guide downloads CLI tools from external URLs.

Mitigation: Verify downloaded tools before installing them, and configure credentials locally without sharing AK/SK in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-obs-dir-count)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [A single integer as plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the count only; counts directories, not files or objects.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
