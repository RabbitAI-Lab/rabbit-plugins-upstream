## Description:

hello-env helps agents run a zero-dependency Bash diagnostic that reports operating system, user, runtime, basic tool, network, container or Kubernetes, workdir, optional config-file, and PVC remount signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect a local machine, CI runner, container, or Kubernetes pod and understand basic environment health. It is especially useful when checking installed tooling, current network context, or whether a Kubernetes PersistentVolume may have been silently remounted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted option or probe value could cause unintended shell command execution.

Mitigation: Use only trusted CLI arguments and trusted HELLO_ENV_PROBE_ENV or --probe-env values; review the script before deployment.

Risk: Probe output may reveal environment-variable values or other local environment details.

Mitigation: Avoid probing secret-bearing variables and review output before sharing logs.

Risk: Snapshot-file handling writes state under the configured workdir or snapshot directory.

Mitigation: Run with a trusted workdir and snapshot directory, and avoid shared or untrusted paths until snapshot handling is reviewed.

Risk: Running the diagnostic with root privileges increases the impact of script bugs.

Mitigation: Run as a non-root user unless elevated privileges are explicitly required and reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/hello-env)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and diagnostic text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local environment diagnostics; no API calls or third-party packages are required.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact documentation)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
