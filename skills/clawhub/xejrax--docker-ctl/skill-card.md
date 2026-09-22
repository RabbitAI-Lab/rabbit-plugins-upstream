## Description:

Inspect containers, logs, and images via podman.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xejrax](https://clawhub.ai/user/xejrax)

### License/Terms of Use:


## Use Case:

Developers and operators use this skill to ask an agent for local podman container, log, image, and inspection guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Container logs and inspect output can expose sensitive application or environment details.

Mitigation: Review and redact agent outputs before sharing them outside the intended local operations context.

Risk: The skill depends on podman being available on the local system.

Mitigation: Confirm podman is installed and target only the intended local containers before running suggested inspection commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xejrax/skills/docker-ctl)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only local container inspection guidance and requires podman.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
