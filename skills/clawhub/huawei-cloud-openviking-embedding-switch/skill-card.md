## Description:

Switches OpenViking's embedding model to a local llama-server or other OpenAI-compatible embedding endpoint, updates the embedding configuration, rebuilds the vector index when dimensions change, restarts the sandboxed service, and verifies the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to migrate OpenViking embeddings to a local or OpenAI-compatible endpoint and recover from embedding-dimension mismatches by rebuilding the affected vector index and verifying service health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can delete the OpenViking vector index and restart the service.

Mitigation: Use it only with an operator who understands the impact, confirms the target model and dimension, and has a recovery plan for the affected index.

Risk: The security review notes weak confirmation, path validation, and recoverable rollback safeguards.

Mitigation: Prefer a dry-run or explicit confirmation flag, canonical path checks for the sandbox directory, and a move-to-backup rollback flow before automated use.

Risk: Incorrect endpoint or dimension choices can leave OpenViking unhealthy or using an incompatible vector index.

Mitigation: Validate the embedding endpoint before modification, measure the actual embedding dimension, back up ov.conf, and verify health, PID change, log status, and collection dimension after restart.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-openviking-embedding-switch)
- [Configuration reference](references/config-reference.md)
- [Guardrails](references/guardrails.md)
- [Verification method](references/verification-method.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [IAM policies and access permissions](references/iam-policies.md)
- [Troubleshooting](references/troubleshooting.md)
- [Related commands](references/related-commands.md)
- [Data flow diagram](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational steps for a local OpenViking and job-env-manager environment; actions may modify configuration, delete the affected vector index, restart the service, and verify health.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
