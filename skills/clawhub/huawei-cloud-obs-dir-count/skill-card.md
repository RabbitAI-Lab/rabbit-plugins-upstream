## Description:

Counts immediate or recursive directories in a Huawei Cloud OBS bucket using hcloud/obsutil or the Huawei Cloud OBS SDK and returns a single numeric count.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and infrastructure teams use this skill to count folders in Huawei Cloud OBS buckets for inventory, structure review, capacity planning, and compliance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs OBS listing access and may reveal bucket directory structure.

Mitigation: Use least-privilege IAM permissions limited to bucket and object listing for the target bucket, and do not grant write or delete actions.

Risk: Huawei Cloud AK/SK credentials could be exposed if pasted into the agent conversation.

Mitigation: Configure credentials in the user's terminal or environment only, avoid sharing secrets in chat, and rotate any credential that is accidentally exposed.

Risk: Installing hcloud or obsutil system-wide can introduce supply-chain or local privilege risk.

Mitigation: Use trusted Huawei Cloud download sources, verify installers where possible, and avoid elevated installation steps unless required by local policy.

Risk: Raw obsutil output can over-count a queried prefix when a zero-byte folder marker exists.

Mitigation: Use the bundled counting script, which excludes the self-entry and includes verification guidance for comparing CLI and SDK results.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/dev-skills-operator/skills/huawei-cloud-obs-dir-count)
- [Publisher Profile](https://clawhub.ai/user/dev-skills-operator)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text count with Markdown guidance and inline shell commands when setup or troubleshooting is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The counting script prints only a single integer on successful execution.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
