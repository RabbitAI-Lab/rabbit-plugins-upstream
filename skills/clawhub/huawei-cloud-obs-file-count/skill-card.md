## Description:

Counts files (objects) in a Huawei Cloud OBS bucket or prefix, excludes folder-marker keys, and returns a single numeric count using KooCLI or the Huawei Cloud OBS SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to count objects in Huawei Cloud OBS buckets or prefixes for inventory, migration planning, cost review, and compliance checks. The skill is read-only and reports only the numeric file count.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may run the bundled count script against Huawei OBS using local cloud credentials.

Mitigation: Use least-privilege OBS credentials limited to list permissions and confirm the intended bucket or prefix before execution.

Risk: Credential exposure could occur if AK/SK values are pasted into the conversation or stored in skill files.

Mitigation: Configure credentials locally in obsutil or environment variables, avoid sharing AK/SK in chat, and keep credentials out of repository files.

Risk: Prerequisite CLI downloads or tools could be obtained from an untrusted source.

Mitigation: Install KooCLI and obsutil from Huawei's official source and verify downloads according to local security practice.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text integer count, with markdown guidance and shell commands when setup or troubleshooting is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The counting script prints only a single integer on success; error guidance is emitted separately on stderr.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
