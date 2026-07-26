## Description: <br>
MinIO AIops helps agents diagnose and operate MinIO object storage, including capacity root-cause analysis, bucket exposure auditing, lifecycle gap analysis, healing checks, service health, per-bucket configuration reads, and governed bucket changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, storage operators, and agents use this skill to inspect MinIO health, capacity pressure, bucket exposure, lifecycle cleanup opportunities, healing status, and selected bucket configuration changes. It is intended for MinIO deployments where the connected access key determines what operations are permitted. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent configured with write-capable MinIO credentials can perform significant bucket changes because the skill does not provide a built-in read-only or approval mode. <br>
Mitigation: Use MinIO IAM to scope credentials to the exact task, prefer read-only keys for diagnosis, and switch to narrowly scoped write credentials only when changes are intended. <br>
Risk: Bucket policy, lifecycle, versioning, quota, purge, and delete operations can affect production data or access. <br>
Mitigation: Use dry-run previews where available, rely on the CLI double-confirmation path for destructive operations, review audit records, and use undo support for reversible changes. <br>
Risk: Credential and master-password handling can expose access to the configured MinIO deployment if operational secrets are mishandled. <br>
Mitigation: Keep secret keys in the encrypted store, protect MINIO_AIOPS_MASTER_PASSWORD, avoid plaintext legacy secret environment variables, and use separate credentials for separate targets. <br>


## Reference(s): <br>
- [MinIO AIops project homepage](https://github.com/AIops-tools/MinIO-AIops) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/minio-aiops) <br>
- [minio-aiops capabilities](references/capabilities.md) <br>
- [minio-aiops CLI reference](references/cli-reference.md) <br>
- [minio-aiops setup & security guide](references/setup-guide.md) <br>
- [Agent guardrails for minio-aiops](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MinIO diagnostic findings, ranked risks, suggested actions, dry-run instructions, and configuration guidance.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
