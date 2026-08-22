## Description:

Switches OpenViking's embedding model to a local llama-server or other OpenAI-compatible embedding endpoint, updates ov.conf, rebuilds incompatible vector index data when dimensions change, restarts the sandboxed server, and verifies the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to change OpenViking embedding models, correct dimension mismatches, rebuild the affected vector index, and verify the service after restart in a controlled local sandbox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can delete OpenViking vector index data when embedding dimensions change.

Mitigation: Use only on a controlled OpenViking sandbox, confirm backups or data rebuild expectations before running, and proceed only after the target embedding endpoint has been validated.

Risk: The skill can kill and restart the OpenViking server, causing service downtime or failed startup.

Mitigation: Run during a maintenance window, verify job-env-manager and SANDBOX_DIR resolve to the expected environment, and use the documented health, PID, dimension, and log checks before considering the switch complete.

Risk: The skill uses a local exec API and depends on correct path resolution in the sandbox.

Mitigation: Restrict use to trusted local environments, validate paths before deletion, and avoid shared or production environments until destructive steps require explicit confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-openviking-embedding-switch)
- [Configuration reference](references/config-reference.md)
- [Guardrails](references/guardrails.md)
- [IAM policies and access permissions](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Troubleshooting](references/troubleshooting.md)
- [Related commands](references/related-commands.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [Example input](demo/example-input.json)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational steps and script usage for a local OpenViking job-env-manager environment.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
