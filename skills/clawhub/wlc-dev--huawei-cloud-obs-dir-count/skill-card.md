## Description:

Counts immediate or recursively nested directories in a Huawei Cloud OBS bucket and returns the count as a number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to check OBS bucket structure for inventory, structure reviews, capacity planning, or compliance checks. It reports directory counts and does not count objects or measure storage size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks this release suspicious because of reported CLI installation and credential-handling practices; the scan did not establish malicious intent.

Mitigation: Review the installation and credential setup before use. Configure credentials in the user's own terminal and grant only the read permissions needed to list bucket contents.

Risk: The security review covered 9 of 10 components, with partial analysis of one shell script.

Mitigation: Review the skill scripts, including the shell scripts, before running them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-obs-dir-count)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Verification Method](artifact/references/verification-method.md)
- [Data Flow Diagram](artifact/references/dataflow-diagram.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Plain text containing a single integer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Counts immediate subdirectories by default; recursive counting is available. Read-only.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
